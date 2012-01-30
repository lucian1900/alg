#!/usr/bin/env python

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({},\n  {},\n  {})' \
            .format(self.value, self.left, self.right)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
