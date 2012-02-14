#!/usr/bin/env python


class Pointer(int):
    '''
    >>> p = Pointer(Heap(), 2, 4); p
    4
    >>> p + 1
    6
    '''

    def __init__(self, heap, sizeof, offset):
        super(Pointer, self).__init__(offset)

        self._heap = heap
        self._sizeof = sizeof

    def __add__(self, other):
        return Pointer(self._heap, self._sizeof, self + self._sizeof * other)

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
        [1, 2]

        >>>
        '''
        self._mem[offset:offset+length] = [0] * length

if __name__ == '__main__':
    import doctest
    doctest.testmod()
