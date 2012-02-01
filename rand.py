#!/usr/bin/python

a = 4
b = 2
m = 7

def lcg(n):
    '''
    >>> lcg(1)
    6

    >>> lcg(3)
    0

    >>> lcg(5)
    1

    '''
    return (a * n + b) % m

if __name__ == '__main__':
    import doctest
    doctest.testmod()
