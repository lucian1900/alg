#!/usr/bin/env python

import re

def valid(email):
    '''
    >>> valid('hello')
    False

    >>> valid('hello@world.com')
    True

    >>> valid('hello@to.')
    True

    >>> valid('hello+world@to.com')
    True

    >>> valid('')
    '''

    pattern = re.compile('''
    ^
    [a-zA-Z0-9_+\.]
    @
    [a-zA-Z0-9\-]
    \.
    [a-zA-Z]?
    $
    ''', re.VERBOSE)

    return pattern.match(email) or False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
