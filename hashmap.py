#!/usr/bin/env python

class HashMap(object):
    '''

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
    def __init__(self, pairs=[], size=8):
        self._length = size
        self._array = [0] * self._length

        for k, v in pairs:
            self[k] = v
    
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
