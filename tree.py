#!/usr/bin/env python

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self, level=0):
        '''Pretty-printing

        >>> Node(1, 2, 3)
        Node(1,
          2,
          3)
        '''
        if isinstance(self.left, Node):
            left = self.left.__repr__(level=level+1)
        else:
            left = repr(self.left)

        if isinstance(self.right, Node):
            right = self.right.__repr__(level=level+1)
        else:
            right = repr(self.right)

        return '{3}Node({0},\n{3}  {1},\n{3}  {2})'.format(
            self.value, left, right, level * '  ')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
