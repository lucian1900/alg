#!/usr/bin/env python

from collections import Mapping

class HashMap(Mapping):
    '''For educational purposes. Similar to CPython's dict in design.

    Tests
    >>> hm = HashMap()
    >>> hm[1] = 2
    >>> hm._array
    [None, (1, 2), None, None, None, None, None, None]

    >>> hm[1]
    2

    >>> hm['hello'] = 'world'
    >>> hm._array
    [None, (1, 2), None, None, None, ('hello', 'world'), None, None]

    >>> h = HashMap([(1, 2), ('hello', 'world')])
    >>> h._array
    [None, (1, 2), None, None, None, ('hello', 'world'), None, None]

    '''
    def __init__(self, mapping=[]):
        self._length = 8
        self._array = [None] * self._length

        self.update(mapping)

    def update(self, mapping):
        try:
            mapping = mapping.items()
        except AttributeError:
            pass

        for k, v in mapping:
            self[k] = v

    def items(self):
        mapping = []
        for i in self._array:
            if i: mapping.append(i)

    def _find(self, key):
        return hash(key) % self._length

    def __getitem__(self, key):
        key, value = self._array[self._find(key)]
        return value

    def __setitem__(self, key, value):
        self._array[self._find(key)] = (key, value)

    def __iter__(self):
        return iter(self._array)

    def __len__(self):
        return len(self._array)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
