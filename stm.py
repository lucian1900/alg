#!/usr/bin/env python

from time import time
from copy import deepcopy
from collections import Mapping


class RetryTransaction(Exception): pass


class Atomic(Mapping):
    '''Transaction context manager and object space proxy

    >>> stm = Atomic({})
    >>> stm['hello'] = [1, 2, 3]; stm['hello']
    [1, 2, 3]

    >>> l = stm['hello']; l
    [1, 2, 3]

    >>> l[0] = 5; l
    [5, 2, 3]

    >>> stm['hello']
    [1, 2, 3]
    '''

    def __init__(self, space):
        self.space = space
        self.log = {}

        self.write_time = 0
        self.read_time = time()

    def __enter__(self):
        self.read_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.write_time >= self.read_time:
            print 'Failing transaction'
        else:
            print 'Commiting'
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
