#!/usr/bin/env python

from time import time
from copy import deepcopy
from collections import Mapping
from functools import wraps


class RetryTransaction(Exception): pass
class FailedTransaction(Exception): pass


class atomic(object):
    '''Decorator for transactions

    >>> s = Store(dict(a=1))
    >>> @atomic(s)
    ... def foo(space):
    ...     space.a += 1
    >>> foo()
    >>> s['a']
    2

    >>> @atomic(s)
    ... def bar(space):
    ...     space.a = 3
    ...     raise RetryTransaction()
    >>> bar()
    Traceback (most recent call last):
    ...
    FailedTransaction
    >>> s['a']
    2
    '''
    def __init__(self, store):
        self.space = Space(store)

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            tries = 0
            commited = False
            while not commited and tries < 5:
                self.space._begin()

                try:
                    result = func(self.space, *args, **kwargs)
                except RetryTransaction:
                    self.space._clear()
                else:
                    commited = self.space._commit()

                tries += 1

            if not commited:
                raise FailedTransaction()

            return result

        return wrap

    def orElse(self, func):
        pass


class Store(object):
    '''Stores names, wrapper for a dict

    TODO Needs locking
    '''
    def __init__(self, items):
        self._items = items
        self._write_time = 0

    def __getitem__(self, key):
        return self._items[key]

    #def __setitem__(self, key, val):
    #    self._items[key] = val

    def update(self, items):
        self._items.update(items)
        self._write_time = time()

class Space(object):
    '''Per-transaction view of the world

    >>> st = Store({'a': 1, 'b': 2})
    >>> s = Space(st); s.a
    1
    >>> s.a = 3; s.a
    3
    >>> st['a']
    1
    '''
    def __init__(self, store):
        self.__dict__['_store'] = store
        self.__dict__['_log'] = {}

    def _begin(self):
        self.__dict__['_read_time'] = time()

    def _commit(self):
        store = self.__dict__['_store']

        if store._write_time >= self.__dict__['_read_time']:
            self.__dict__['_clear']()
            return False
        else:
            store.update(self.__dict__['_log'])
            return True

    def _clear(self):
        self.__dict__['_log'].clear()

    def __getattr__(self, key):
        try:
            return self.__dict__['_log'][key]
        except KeyError:
            return self.__dict__['_store'][key]

    def __setattr__(self, key, val):
        self.__dict__['_log'][key] = val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
