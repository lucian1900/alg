#!/usr/bin/env python

class Heap(object):
    '''

    >>> Heap().get_children(0)
    ()

    >>> Heap([1]).get_children(0)
    ()

    >>> Heap([1, 2, 3]).get_children(0)
    (1, 2)

    >>> Heap([1, 2, 3]).get_children(1)
    ()

    >>> Heap([1, 2, 3, 4, 5]).get_children(1)
    (3, 4)

    >>> h = Heap(); h.push(1); h.pop()
    1

    >>> Heap([5, 2, 1, 7, 4, 3, -2])._array
    [-2, 4, 1, 7, 5, 3, 2]

    >>> #list(Heap([5, 2, 1, 7, 4, 3, -2]))
    [-2, 1, 2, 3, 4, 5, 7]
    '''

    def __init__(self, items=[]):
        self._array = []

        for i in items:
            self.push(i)

    def push(self, item):
        self._array.append(item)
        i = len(self._array) - 1

        while i != 0:
            parent = self.get_parent(i)

            if self._array[i] < self._array[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def pop(self):
        if len(self._array) == 0:
            raise IndexError('pop from empty Heap')

        result = self._array[0]
        if len(self._array) == 1:
            return result

        self._array[0] = self._array.pop()

        i = 0
        while i < len(self._array):
            try:
                smallest = self.get_children(i)[0]
            except IndexError:
                break

            if self._array[smallest] < self._array[i]:
                self.swap(i, smallest)
                i = smallest

        return result

    def swap(self, a, b):
        self._array[a], self._array[b] = self._array[b], self._array[a]

    def get_parent(self, i):
        return (i - 1) // 2

    def get_children(self, i):
        left = 2 * i + 1
        right = left + 1

        if right >= len(self._array):
            if left >= len(self._array):
                return ()

            return (left,)

        if self._array[left] < self._array[right]:
            return left, right
        else:
            return right, left

    def __iter__(self):
        h = Heap(self._array)

        while True:
            yield h.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
