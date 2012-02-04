#!/usr/bin/env python

import os
from mmap import mmap

class Heap(object):
    def __init__(self, filename):
        if not os.path.exists(filename):
            f = open(filename, 'w')
            f.write('\x00')
            f.close()

        self.file = open(filename, 'r+')
        self.map = mmap(self.file.fileno(), 0)

    def get(self, key):
        pass


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
