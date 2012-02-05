#!/usr/bin/env python

from time import time
from copy import deepcopy
from collections import Mapping
from functools import wraps


class RetryTransaction(Exception): pass


class atomic(object):
    '''Decorator for transactions

    >>> s = Space(a=1)
    >>> @atomic(s)
    ... def foo(space):
    ...     space.a += 1
    >>> foo()
    >>> s.a
    2

    >>> @atomic(s)
    ... def bar(space):
    ...     space.a = 3
    ...     raise RetryTransaction()
    >>> foo()
    >>> s.a
    2
    '''
    def __init__(self, space):
        self.space = space

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
                    retry = True
                except Exception, e:
                    retry = True
                else:
                    retry = False

                commited = self.space._commit(retry=retry)

                tries += 1

            return result

        return wrap

    def orElse(self, func):
        pass


class Space(object):
    '''Transaction object space'''

    def __init__(self, **space):
        self.__dict__['_store'] = space
        self.__dict__['_log'] = {}

        self.__dict__['_write_time'] = 0
        self.__dict__['_read_time'] = time()

    def _begin(self):
        self.__dict__['_read_time'] = time()

    def _commit(self, retry=False):
        if retry or \
                self.__dict__['_write_time'] >= self.__dict__['_read_time']:
            self.__dict__['_log'].clear()
        else:
            self.__dict__['_store'].update(self.__dict__['_log'])
            self.__dict__['_write_time'] = time()

    def __getattr__(self, key):
        return deepcopy(self.__dict__['_store'][key])

    def __setattr__(self, key, val):
        self.__dict__['_log'][key] = val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
