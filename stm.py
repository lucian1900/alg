#!/usr/bin/env python

import time
import threading
import functools
import copy

class RetryTransaction(Exception): pass
class FailedTransaction(Exception): pass


class atomic(object):
    '''Decorator for transactions

    Working transaction
    >>> s = Store(a=1)
    >>> @atomic(s)
    ... def inc(space):
    ...     space.a += 1
    ...     return space.a
    >>> inc()
    2
    >>> s['a']
    2

    Failing transaction (retries too much)
    >>> @atomic(s)
    ... def fail(space):
    ...     space.a = 3
    ...     raise RetryTransaction()
    >>> fail()
    Traceback (most recent call last):
    ...
    FailedTransaction
    >>> s['a']
    2

    Transaction failure across threads
    >>> s = Store(i=0)
    >>> @atomic(s)
    ... def inc(space):
    ...     space.i += 1
    >>> @atomic(s)
    ... def slowinc(space):
    ...     time.sleep(1)
    ...     space.i += 2
    >>> threading.Thread(target=slowinc).start()
    >>> #inc()
    >>> #time.sleep(2); s['i']
    1
    '''

    def __init__(self, store, max_retries=15):
        self.space = Space(store)
        self.max_retries = max_retries

    def __call__(self, func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            tries = 0
            commited = False
            while not commited and tries < self.max_retries:
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

    '''
    def __init__(self, items=None, **kwargs):
        if kwargs:
            self._items = kwargs
        else:
            self._items = items

        self._write_time = 0
        self._lock = threading.Lock()

    def __getitem__(self, key):
        return self._items[key]

    #def __setitem__(self, key, val):
    #    self._items[key] = val

    def update(self, items):
        self._items.update(items)
        self._write_time = time.time()

class Space(object):
    '''Per-transaction view of the world

    >>> st = Store(a=1, b=2)
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
        self.__dict__['_read_time'] = time.time()

    def _commit(self):
        store = self.__dict__['_store']

        with store._lock:
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
            return copy.deepcopy(self.__dict__['_store'][key])

    def __setattr__(self, key, val):
        self.__dict__['_log'][key] = val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
