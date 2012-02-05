#!/usr/bin/env python

from collections import Mapping
from copy import deepcopy

class Space(Mapping):
    '''STM object space

    >>> stm = Space()

    >>> stm['hello'] = [1, 2, 3]
    >>> stm['hello']
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
        self.space = {}

    def __getitem__(self, key):
        val = self.space[key]
        return deepcopy(val)

    def __setitem__(self, key, val):
        val = deepcopy(val)
        self.space[key] = val

    def __len__(self):
        return len(self.space)

    def __iter__(self):
        return iter(self.space)

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        for key, val in self.space.iteritems():
            yield key, deepcopy(val)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
