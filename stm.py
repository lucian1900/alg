#!/usr/bin/env python

from collections import Mapping
from copy import deepcopy


class Atomic(Mapping):
    '''Transaction context manager. Implements STM semantics on top of
    an object space (currently a dict). Might even work with locals()

    >>> stm = Atomic({})
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

    def __init__(self, space):
        self.space = space

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

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
