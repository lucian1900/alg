#!/usr/bin/env python


def test(matcher):
    data = [
        ('abc', 'abecedarabcsd', 8),
        ('abc', 'abecedar', -1),
    ]

    for pattern, string, result in data:
        if matcher(pattern, string) != result:
            return False

    return True


def hash_step(c):
    return ord(c)


def hash_naive(s):
    h = 0
    for c in s:
        h += hash_step(c)
    return h


def rabin_karp_naive(pattern, string):
    '''
    >>> test(rabin_karp_naive)
    True

    '''
    pattern_len = len(pattern)  # cache
    string_len = len(string)

    pattern_hash = hash_naive(pattern)
    sample_hash = hash_naive(string[:pattern_len - 1])

    for i in range(string_len - pattern_len):
        sample = string[i:pattern_len + i]
        sample_hash += hash_step(sample[-1])

        if sample_hash == pattern_hash and sample == pattern:
            return i

        sample_hash -= hash_step(sample[0])

    return -1

BASE = 31


def hash_roll(h, prev, l, next):
    return BASE * (h - prev * BASE ** l) + next


def hash_rolling(chars):
    '''
    >>> first = hash_rolling('abc')
    >>> second = hash_rolling('bcd')
    >>> second == hash_roll(first, ord('a'), 2, ord('d'))
    True
    '''
    h = 0
    l = len(chars)
    for i, char in enumerate(chars):
        h += ord(char) * BASE ** (l - i - 1)
    return h


def rabin_karp_rolling(pattern, string):
    '''
    >>> test(rabin_karp_rolling)
    True
    '''
    pattern_len = len(pattern)  # cache
    string_len = len(string)

    pattern_hash = hash_rolling(pattern)
    sample = string[:pattern_len]
    sample_hash = hash_rolling(sample)

    for i in range(pattern_len, string_len):
        if sample_hash == pattern_hash and sample == pattern:
            return i - pattern_len

        char = string[i]
        sample_hash = hash_roll(
            sample_hash,
            ord(sample[0]), pattern_len - 1,
            ord(char),
        )
        sample = sample[1:] + char

    return -1


def make_kmp_table(pattern):
    '''
    >>> make_kmp_table('abcdabd')
    [-1, 0, 0, 0, 0, 1, 2]
    '''
    table = [-1, 0]
    pos = 2
    cand = 0  # Next candidate substring index
    while pos < len(pattern):
        # Substring continues
        if pattern[pos - 1] == pattern[cand]:
            table.append(cand + 1)
            pos += 1
            cand += 1

        # But we can fall back
        elif cand > 0:
            cand = table[cand]

        # No more candidates
        else:
            table.append(0)
            pos += 1

    return table


def knuth_morris_pratt(pattern, string):
    '''
    >>> test(knuth_morris_pratt)
    True
    '''
    table = make_kmp_table(pattern)
    pattern_len = len(pattern)  # cache
    string_len = len(string)

    for i in range(string_len - pattern_len):
        for j, char in enumerate(pattern):
            if string[i + j] != char:
                shift = table[j]
                if shift > -1:
                    i += table[j]
                break
            elif j == pattern_len - 1:
                return i

    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
