#!/usr/bin/env python

class Heap(object):
    def __init__(self):
        self._array = []

    def add(self, item):
        self._array.append(item)

    def get_parent(self, i):
        return (i - 1) // 2

    def get_children(self, i):
        return 2 * i + 1, 2 * i + 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
