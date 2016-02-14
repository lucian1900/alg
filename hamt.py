#!/usr/bin/python


class Node(object):
    pass


class Leaf(Node):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Array(Node):
    def __init__(self, leaves):
        self.leaves = leaves


if __name__ == '__main__':
    import doctest
    doctest.testmod()
