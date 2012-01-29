#!/usr/bin/env python

class Heap(object):
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
        result = self._array[0]

        self._array[0] = self._array.pop()

        i = 0
        while i < len(self._array):
            li, ri = self.get_children(i)
            left = self._array[li]
            right = self._array[ri]
            current = self._array[i]

            if current < left and current < right:
                break
            elif left < right:
                self.swap(i, li)
            else:
                self.swap(i, ri)


        return result

    def swap(self, a, b):
        self._array[a], self._array[b] = self._array[b], self._array[a]

    def get_parent(self, i):
        return (i - 1) // 2

    def get_children(self, i):
        return 2 * i + 1, 2 * i + 2

    def __iter__(self):
        array = self._array[:]
        while len(self._array) > 0:
            yield self.pop()
        self._array = array


if __name__ == '__main__':
    import doctest
    doctest.testmod()
