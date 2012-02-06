#!/usr/bin/env python

from random import shuffle


def bits(n):
    return bin(n + 2**32)[-32:]


def addxor(s):
    h = 0
    for c in s:
        i = ord(c)
        h = h ^ i + i
    return h


t = range(255)
shuffle(t)

def pearson(s):
    h = 0
    for c in s:
        i = h ^ ord(c)
        h = t[i]
    return h


def javastr(s):
    h = 0
    for c in s:
        h = 31 * h + ord(c)
    return h
