#!/usr/bin/env python


class Pointer(object):
    '''
    >>> p = Pointer(Heap(range(10)), 2, 4); p
    4
    >>> p + 1
    6
    >>> p.contents
    [4, 5]
    >>> p.contents = [-2, -3]; p.contents
    [-2, -3]
    '''

    def __init__(self, heap, size, address):
        self._heap = heap
        self._size = size
        self._addr = address

    def __int__(self):
        return self._addr

    def __add__(self, other):
        offset = int(other) * self._size + self._addr
        return Pointer(self._heap, self._size, offset)

    def __repr__(self):
        return repr(self._addr)

    @property
    def contents(self):
        return self._heap[self._addr : self._addr+self._size]

    @contents.setter
    def contents(self, value):
        self._heap[self._addr : self._addr+self._size] = value


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
        if offset + length <= len(self):
            self[offset:offset+length] = [0] * length

if __name__ == '__main__':
    import doctest
    doctest.testmod()
