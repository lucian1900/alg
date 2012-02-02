#!/usr/bin/env python

def feasible(queens, k):
    '''
    >>> feasible([1, 3, 0], 2)
    True

    >>> feasible([1, 3, 0], 1)
    False
    '''
    for i in xrange(k):
        if queens[i] == queens[k] \
                or queens[i] - i == queens[k] - k \
                or queens[i] + i == queens[k] + k:
            return False

    return True

def nqueens(queens, k=0):
    '''
    >>> nqueens([0] * 4)
    [1, 3, 0, 2]
    '''
    if k == len(queens):
        return queens

    for i in xrange(len(queens)):
        queens[k+1] = i
        if feasible(queens, k + 1):#queens
            return nqueens(queens, k + 1)

    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
