#!/usr/bin/python

a = 4
b = 2
m = 7

def lcg(n):
    '''
    >>> lcg(1)

    >>> lcg(3)

    >>> lcg(5)

    '''
    return (a * n + b) % 7

if __name__ == '__main__':
    pass
