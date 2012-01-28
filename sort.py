#!/usr/bin/env python

def test(sort):
    arrays = [
        [],
        [1],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 6, 3, 4, 5, 2, 7, 8, 9, 10],
        [5, 2, 9, 6, 10, 4, 3, 1, 8, 7],
        [2, 10, 4, 6, 3, 8, 1, 5, 7, 9, 2],
    ]

    for i in arrays:
        if sort(i) != sorted(i):
            return False

    return True


def swap(array, x, y):
    array[y], array[x] = array[x], array[y]


def bubble(array):
    '''Naive bubblesort. O(n^2)

    >>> test(bubble)
    True
    '''
    while True:
        no_swap = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i+1)
                no_swap = False

        if no_swap:
            return array


def selection(array):
    '''Naive selection.

    >>> test(selection)
    True
    '''
    for i, e in enumerate(array):
        min_val = e
        min_pos = i

        for j in range(i, len(array)):
            if array[j] < min_val:
                min_val = array[j]
                min_pos = j

        swap(array, i, min_pos)

    return array


def insertion(array):
    '''Naive insertion.

    >>> test(insertion)
    True
    '''
    return array


def quick(array):
    '''Naive recursive version. Middle is chosen as pivot

    >>> test(quicksort)
    True

    '''

    if len(array) <= 1:
        return array

    pivotIndex = len(array) / 2
    pivot = array[pivotIndex]

    less = []
    more = []
    for i in array[:pivotIndex] + array[pivotIndex + 1:]:
        if i < pivot:
            less.append(i)
        else:
            more.append(i)

    return quick(less) + [pivot] + quick(more)


def partition(array, left, right, pivotIndex):
    pivot = array[pivotIndex]

    swap(array, pivotIndex, right) # move pivot to end
    pivotIndex = left

    for i in range(left, right):
        if array[i] < pivot:
            swap(array, i, pivotIndex)
            pivotIndex += 1

    swap(array, pivotIndex, right) # move pivot to final position

    return pivotIndex

def quick_inplace(array, left=0, right=None):
    '''In place (no copies/concats). Uses partition function.

    #>>> test(quicksort_inplace)
    True
    '''
    if not right:
        right = len(array) - 1

    pivotIndex = (left + right) / 2
    pivotIndex = partition(array, left, right, pivotIndex)

    quick_inplace(array, left, pivotIndex - 1)
    quick_inplace(array, pivotIndex + 1, right)


def merge_bottomup(array, chunked=False):
    '''Naive mergesort

    >>> test(mergesort_bottomup)
    True
    '''

    if not chunked:
        # wrap each element in a list
        array = [[e] for e in array]

    if len(array) <= 1:
        if len(array) == 1:
            # unwrap
            array = array[0]

        return array

    while True:
        try:
            left = iterator.next()
        except StopIteration:
            break

        try: # for odd length arrays
            right = iterator.next()
        except StopIteration:
            right = []

        merged = []
        while len(left) != 0 and len(right) != 0:
            if len(left) > 0:
                l = left[0]
                left = left[1:]
            else:
                l = None # less than anything

            if len(right) > 0:
                r = right[0]
                right = right[1:]
            else:
                r = None

            merged.append(min(l, r))

        array = [merged] + array

    merge_bottomup(array, chunked=True)

def tim(array):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
