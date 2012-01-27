#!/usr/bin/env python

class HashMap(object):
    '''

    >>> hm = HashMap()
    >>> hm[1] = 2
    >>> hm[1]
    2
    '''
    def __init__(self):
        self._array = [0]*8
        self._length = 8
    
    def _find(self, key):
        return hash(key) % self._length

    def __getitem__(self, key):
        return self._array[self._find(key)][1]

    def __setitem__(self, key, value):
        self._array[self._find(key)] = (key, value)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
