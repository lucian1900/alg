#!/usr/bin/python
from __future__ import division

import random


def test(median):
    arrays = [
        [random.randint(0, 100) for _ in range(n)]
        #for n in [0, 10, 100, 1000]
        for n in [100]
    ]

    for i in arrays:
        if len(i) == 0:
            continue

        if median(i) != sorted(i)[len(i) // 2]:
            return False

    return True


def swap(array, x, y):
    array[y], array[x] = array[x], array[y]


def split_array(array, n=10):
    chunk_len = len(array) // n
    left = 0
    right = chunk_len
    nodes = []
    for _ in xrange(n):
        nodes.append(array[left:right])
        left = right
        right = left + chunk_len
    return nodes


def merge_median_par(array, n=10):
    '''Parallel simulation of merge select median.
    >>> test(merge_median_par)
    True
    '''
    # Each node gets a chunk
    nodes = split_array(array, n)
    for node in nodes:
        # Nodes sort their chunk
        node.sort()
    # The rest works as following:
    # - ask for the lowest value from each node
    # - pick the lowest value
    #   - tell that node to remove the value
    # - if we've seen n/2+1 values so far, this is our median
    node_i = {x: 0 for x in xrange(n)}
    median = None
    for _ in xrange(len(array) // 2 + 1):
        vals = sorted(
            (nodes[node][i], node)
            for node, i in node_i.iteritems()
        )
        median, node_index = vals[0]
        node_i[node_index] += 1
    return median


if __name__ == '__main__':
    import doctest
    doctest.testmod()
