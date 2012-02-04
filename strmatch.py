#!/usr/bin/env python

def hash(s):
    h = 0
    for c in s:
        h = hash_step(h, c)
    return h

def hash_step(h, c, direction=1):
    return h + direction * ord(c)

def robin_karp(pattern, string):
    '''
    >>> robin_karp('abc', 'abecedarabcsd')
    8

    >>> robin_karp('abc', 'abecedar')
    -1

    '''
    pattern_len = len(pattern) #cache
    string_len = len(string)

    pattern_hash = hash(pattern)
    sample_hash = hash(string[:pattern_len - 1])

    for i in range(string_len - pattern_len):
        sample = string[i:pattern_len+i]
        sample_hash = hash_step(sample_hash, sample[-1:])

        if sample_hash == pattern_hash:
            if sample == pattern:
                return i

        sample_hash = hash_step(sample_hash, sample[0], direction=-1)

    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
