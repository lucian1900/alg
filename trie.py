#!/usr/bin/env python

from collections import Mapping

class Trie(Mapping):
    '''
    >>> t = Trie()
    '''

    def __getitem__(self, key):
        pass

    def __len__(self):
        return 0

    def __iter__(self):
        return iter([])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
