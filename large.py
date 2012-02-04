#!/usr/bin/env python

import os
from mmap import mmap, ACCESS_READ

class Heap(object):
    key_size = 3
    count_size = 10
    offset = key_size + count_size

    def __init__(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                f.write('\x00')

        self.file = open(filename, 'r+b')
        self.map = mmap(self.file.fileno(), 0)

    def incr(self, key):
        item_key = key.ljust(self.key_size)

        for i, (k, c) in enumerate(self):
            if k == key:
                self.map.seek(i)
                self.map.write(item_key + self.pad(c + 1))
                return

        size = self.map.size()
        if size == 1: size = 0

        self.map.resize(size + self.offset)
        self.map.seek(self.map.size() - self.offset)
        self.map.write(item_key + self.pad(1))

    def pad(self, count):
        return repr(count).zfill(self.count_size)

    def __iter__(self):
        if self.map.size() == 1:
            return

        i = 0
        while i < self.map.size():
            self.map.seek(i)
            item = self.map.read(self.offset)
            print item
            k, c = item[:self.key_size], item[self.key_size+1: self.offset]
            yield k.rstrip(), int(c)

            i += self.offset


def process(filename='/home/lucian/Prog/alg/large.in'):
    f = open(filename, 'r')
    m = mmap(f.fileno(), 0, access=ACCESS_READ)
    h = Heap('/home/lucian/Prog/alg/large.out')

    while m.tell() < 1000:#m.size():
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
    #gendata()
    process()
