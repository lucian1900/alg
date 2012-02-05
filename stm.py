#!/usr/bin/env python

from time import time
from copy import deepcopy
from collections import Mapping


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

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getitem__(self, key):
        self.read_time = time()

        return deepcopy(self.space[key])

    def __setitem__(self, key, val):
        self.space[key] = deepcopy(val)

    def __len__(self):
        return len(self.space)

    def __iter__(self):
        return iter(self.space)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
