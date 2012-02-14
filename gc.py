#!/usr/bin/env python

class Heap(object):
    def __init__(self, initial=None):
        self._mem = initial or []

    def alloc(self, size):
        '''malloc equivalent

        >>> h = Heap(); h.alloc(2)
        [0, 0]
        '''
        chunk = [0] * size
        self._mem.extend(chunk)
        return chunk

    def free(self, offset, length):
        '''
        >>> h = Heap([1, 0, 4, 5, 1, 2, 3]); h.free(3, 2); h._mem
        [1, 0, 4, 0, 0, 2, 3]

        >>> h = Heap([1, 2]); h.free(4, 1); h._mem

        '''
        self._mem[offset:offset+length] = [0] * length

if __name__ == '__main__':
    import doctest
    doctest.testmod()
