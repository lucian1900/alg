#!/usr/bin/env python


class Pointer(object):
    '''
    >>> p = Pointer(Heap(), 2, 4); p
    4
    >>> p + 1
    6
    '''

    def __init__(self, heap, sizeof, offset):
        self._heap = heap
        self._sizeof = sizeof
        self._offset = offset

    def __int__(self):
        return self._offset

    def __add__(self, other):
        offset = int(other) * self._sizeof + self._offset
        return Pointer(self._heap, self._sizeof, offset)

    def __repr__(self):
        return repr(self._offset)

    @property
    def contents(self):
        return self._heap[self._offset : self._offset+self._sizeof]

    @contents.setter
    def contents(self, value):
        self._heap[self._offset : self._offset+self._sizeof] = value


class Heap(list):
    def alloc(self, size):
        '''malloc equivalent

        >>> h = Heap(); h.alloc(2)
        [0, 0]
        '''
        chunk = [0] * size
        self.extend(chunk)
        return chunk

    def free(self, offset, length):
        '''
        >>> h = Heap([1, 0, 4, 5, 1, 2, 3]); h.free(3, 2); h
        [1, 0, 4, 0, 0, 2, 3]

        >>> h = Heap([1, 2]); h.free(4, 1); h
        [1, 2]

        >>>
        '''
        self[offset:offset+length] = [0] * length

if __name__ == '__main__':
    import doctest
    doctest.testmod()
