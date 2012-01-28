#!/usr/bin/env python

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrays = [
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 6, 3, 4, 5, 2, 7, 8, 9, 10],
    [5, 2, 9, 6, 10, 4, 3, 1, 8, 7],
    [2, 10, 4, 6, 3, 8, 1, 5, 7, 9],
]

def quicksort(array):
    '''Naive recursive version. Middle is chosen as pivot

    >>> for i in arrays:
    ...     if quicksort(i) != sorted_array:
    ...         print False

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

    return quicksort(less) + [pivot] + quicksort(more)


def swap(array, x, y):
    array[y], array[x] = array[x], array[y]

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

def quicksort_inplace(array, left=0, right=None):
    '''In place (no copies/concats). Uses partition function.

    >>> for i in arrays:
    ...     if quicksort_inplace(i) != sorted_array:
    ...         print False
    '''
    if not right:
        right = len(array) - 1

    pivotIndex = (left + right) / 2
    pivotIndex = partition(array, left, right, pivotIndex)

    quicksort_inplace(array, left, pivotIndex - 1)
    quicksort_inplace(array, pivotIndex + 1, right)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
