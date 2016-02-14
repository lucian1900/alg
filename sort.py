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
        for i in xrange(len(array) - 1):
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
    for i, e in enumerate(array):
        j = i
        while j > 0 and e < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1

    return array


def quick(array):
    '''Naive recursive version. Middle is chosen as pivot

    >>> test(quick)
    True

    '''

    if len(array) <= 1:
        return array

    pivot_index = len(array) / 2
    pivot = array[pivot_index]

    less = []
    more = []
    for i in array[:pivot_index] + array[pivot_index + 1:]:
        if i < pivot:
            less.append(i)
        else:
            more.append(i)

    return quick(less) + [pivot] + quick(more)


def partition(array, left, right, pivot_index):
    pivot = array[pivot_index]

    # Move pivot to end
    swap(array, pivot_index, right)
    pivot_index = left

    for i in xrange(left, right):
        if array[i] < pivot:
            swap(array, i, pivot_index)
            pivot_index += 1

    # Move pivot to final position
    swap(array, pivot_index, right)

    return pivot_index


def quick_inplace(array, left=0, right=None):
    '''In place (no copies/concats). Uses partition function.

    #>>> test(quicksort_inplace)
    True
    '''
    if not right:
        right = len(array) - 1

    pivot_index = (left + right) / 2
    pivot_index = partition(array, left, right, pivot_index)

    quick_inplace(array, left, pivot_index - 1)
    quick_inplace(array, pivot_index + 1, right)


def merge(left, right):
    '''Merge sorted lists
    >>> l1 = [1, 2, 4]
    >>> l2 = [3, 5]
    >>> merge(l1, l2)
    [1, 2, 3, 4, 5]
    '''
    result = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # copy possible remainder
    result += left[i:]
    result += right[j:]

    return result


def mergesort(array):
    '''Naive mergesort, top to bottom
    >>> test(mergesort)
    True
    '''
    if len(array) <= 1:
        return array

    mid = len(array) / 2

    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    return merge(left, right)


def mergesort_bottomup(array):
    '''Iterative mergesort
    >>> test(mergesort_bottomup)
    True
    '''
    if len(array) == 0:
        return array

    array = [[i] for i in array]

    while len(array) > 1:
        try:
            left = array.pop(0)
        except IndexError:
            left = []
        try:
            right = array.pop(0)
        except IndexError:
            right = []

        array.insert(0, merge(left, right))

    return array[0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
