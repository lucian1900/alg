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
    False
    '''

    pattern = re.compile('''
    ^
    ([a-zA-Z0-9_+\.\-]+
    @
    [a-zA-Z0-9\-]+
    \.
    [a-zA-Z]*)
    $
    ''', re.VERBOSE)

    match = pattern.match(email)
    if match == None:
        return False

    else:
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
