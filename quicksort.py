#!/usr/bin/env python

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrays = [
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 6, 3, 4, 5, 2, 7, 8, 9, 10],
    [5, 2, 9, 6, 10, 4, 3, 1, 8, 7],
    [2, 10, 4, 6, 3, 8, 1, 5, 7, 9],
]

def quicksort(array):
    '''
    >>> for i in arrays:
    ...     if quicksort(i) != sorted_array:
    ...         print False
    '''

    if len(array) <= 1:
        return array

    mid = len(array) / 2
    pivot = array[mid]

    less = []
    more = []
    for i in array[:mid] + array[mid+1:]:
        if i < pivot:
            less.append(i)
        else:
            more.append(i)

    return quicksort(less) + [pivot] + quicksort(more)

def quicksort_inplace(array):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
