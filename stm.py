#!/usr/bin/env python

from collections import Mapping
from copy import deepcopy


class Atomic(Mapping):
    '''Transaction context manager and object space proxy

    '''

    def __init__(self, space):
        self.space = space

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, val):
        pass

    def __len__(self):
        return len(self.space)

    def __iter__(self):
        return iter(self.space)


class Space(Mapping):
    '''STM object space

    >>> stm = Space()
    >>> stm['hello'] = [1, 2, 3]; stm['hello']
    [1, 2, 3]

    >>> list(stm)
    ['hello']

    >>> list(stm.items())
    [('hello', [1, 2, 3])]

    >>> l = stm['hello']; l
    [1, 2, 3]

    >>> l[0] = 5; l
    [5, 2, 3]

    >>> stm['hello']
    [1, 2, 3]
    '''

    def __init__(self):
        self.store = {}

    def __getitem__(self, key):
        val = self.store[key]
        return deepcopy(val)

    def __setitem__(self, key, val):
        val = deepcopy(val)
        self.store[key] = val

    def __len__(self):
        return len(self.store)

    def __iter__(self):
        return iter(self.store)

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        for key, val in self.store.iteritems():
            yield key, deepcopy(val)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
