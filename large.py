#!/usr/bin/env python

import os
from mmap import mmap, ACCESS_READ

class Heap(object):
    key_size = 3
    count_size = 10
    offset = key_size + count_size

    def __init__(self, filename):
        if not os.path.exists(filename):
            f = open(filename, 'wb')
            f.write('\x00')
            f.close()

        self.file = open(filename, 'r+b')
        self.map = mmap(self.file.fileno(), 0)

    def incr(self, key):
        size = self.map.size()

        if size < size + self.offset:
            self.map.resize(size + self.offset)

        item = key.ljust(self.key_size) + self.pad(1)

        self.map.write(item)

    def pad(self, count):
        return repr(count).zfill(self.count_size)

    def __iter__(self):
        i = 0
        while i < self.map.size():
            yield self.map[i:i+self.offset]
            i += self.offset


def process(filename='/home/lucian/Prog/alg/large.in'):
    f = open(filename, 'r')
    m = mmap(f.fileno(), 0, access=ACCESS_READ)
    h = Heap('/home/lucian/Prog/alg/large.out')

    while m.tell() < m.size():
        line = m.readline()
        key = line.split('\n')[0]

        h.incr(key)


def gendata(filename='/home/lucian/Prog/input'):
    import random

    f = open(filename, 'w')

    i = 0
    while i < 1000000000:
        j = 0
        bound = random.randint(0, 100)
        while j < bound:
            f.write(str(bound))
            f.write('\n')
            j += 1

        i += 1

    f.close()

if __name__ == '__main__':
    gendata()
    #import doctest
    #doctest.testmod()
