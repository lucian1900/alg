#!/usr/bin/env python

class HashMap(object):
    '''For educational purposes. Similar to CPython's dict in design.

    Tests
    >>> hm = HashMap()
    >>> hm[1] = 2
    >>> hm._array
    [0, (1, 2), 0, 0, 0, 0, 0, 0]
    
    >>> hm[1]
    2

    >>> hm['hello'] = 'world'
    >>> hm._array
    [0, (1, 2), 0, 0, 0, ('hello', 'world'), 0, 0]
    
    >>> h = HashMap([(1, 2), ('hello', 'world')])
    >>> h._array
    [0, (1, 2), 0, 0, 0, ('hello', 'world'), 0, 0]
    
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
