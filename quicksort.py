#!/usr/bin/env python

arrays = [
    [1, 6, 3, 4, 5, 2, 7, 8, 9, 10],
]

def quicksort(array):
    '''
    >>> quicksort(arrays[0])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
