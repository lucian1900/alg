#!/usr/bin/env python

class Heap(object):
    def __init__(self):
        self._mem = []

    def alloc(self, size):
        '''malloc equivalent

        >>> h = Heap(); h.alloc(2)
        [0, 0]
        '''
        chunk = [0] * size
        self._mem.extend(chunk)
        return chunk

if __name__ == '__main__':
    import doctest
    doctest.testmod()
