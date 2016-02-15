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

        correct = sorted(i)[len(i) // 2]
        result = median(i)
        if result != correct:
            return False

    return True


def swap(array, x, y):
    array[y], array[x] = array[x], array[y]


def split_array(array, n=10):
    '''Only correct if len(array) is a multiple of n.'''
    chunk_len = len(array) // n
    left = 0
    right = chunk_len
    nodes = []
    for _ in xrange(n):
        nodes.append(array[left:right])
        left = right
        right = left + chunk_len
    return nodes


def partition(array, pivot):
    left, right = [], []
    all_pivot = True
    for v in array:
        if v != pivot:
            all_pivot = False
        if v < pivot:
            left.append(v)
        else:
            right.append(v)
    return left, right, all_pivot


def quick_median_rec(array):
    '''
    >>> test(quick_median_rec)
    True
    '''
    median = len(array) // 2
    while True:
        pivot = random.choice(array)
        left, right, all_pivot = partition(array, pivot)
        if len(right) == median or all_pivot:
            return pivot
        if len(right) > median:
            array = right
        else:
            median = median - len(right)
            array = left


def quick_median_rec_par(array, n=10):
    '''Parallel simulation of quick select median. Not in-place.
    >>> test(quick_median_rec_par)
    True
    '''
    nodes = split_array(array, n)
    median = len(array) // 2
    while True:
        # Select random pivot
        pivot = random.choice(random.choice(filter(len, nodes)))
        nodes_p = []
        left, right = 0, 0
        # Ask nodes for # on left and right of pivot
        all_pivot = []
        for node in nodes:
            l, r, ap = partition(node, pivot)
            all_pivot.append(ap)
            left += len(l)
            right += len(r)
            nodes_p.append((l, r))
        if right == median or all(all_pivot):
            return pivot
        if left == 0 or right == 0:
            continue
        if right > median:
            keep = 1
        else:
            median = median - right
            keep = 0
        # Ask nodes to throw away the smaller half
        nodes = []
        for halves in nodes_p:
            nodes.append(halves[keep])


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
