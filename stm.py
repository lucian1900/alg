#!/usr/bin/env python

from time import time
from copy import deepcopy
from collections import Mapping


class RetryTransaction(Exception): pass
class DictWrapper(dict): pass


class atomic(object):
    '''Decorator for transactions

    >>> s = Space({'a', 1})
    >>> @atomic(s)
    ... def foo(space):
    ...     space['a'] += 1
    >>> foo()
    >>> s['a']
    2
    '''
    def __init__(self, space):
        self.space = space

    def __call__(self, func):
        def wrap(*args, **kwargs):
            result = func(self.space, *args, **kwargs)

            if self.space.write_time >= self.space.read_time:
                print 'Failing transaction'
            else:
                self.space.space.update(self.space.log)
                self.space.write_time = time()

        return wrap


class Space(Mapping):
    '''Transaction object space

    '''

    def __init__(self, space):
        self.space = space
        self.log = {}

        self.write_time = 0
        self.read_time = time()

    def __enter__(self):
        self.read_time = time()

    def __commit__(self):
        if self.write_time >= self.read_time:
            print 'Failing transaction'
        else:
            self.space.update(self.log)
            self.write_time = time()

    def __getitem__(self, key):
        return deepcopy(self.space[key])

    def __setitem__(self, key, val):
        self.log[key] = val

    def __len__(self):
        return len(self.space)

    def __iter__(self):
        return iter(self.space)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
