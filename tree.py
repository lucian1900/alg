#!/usr/bin/env python

class Node(object):
    '''

    >>> b = Node(1, 2, 3)
    >>> b.left
    2
    >>> b.right = 4
    >>> b.children
    [2, 4]

    '''

    def __init__(self, value, *children):
        self.value = value
        self.children = list(children)

    def _check_binary(self):
        if len(self.children) != 2:
            raise ValueError('node is not binary')

    @property
    def left(self):
        self._check_binary()

        return self.children[0]

    @left.setter
    def left(self, value):
        self._check_binary()

        self.children[0] = value

    @property
    def right(self):
        self._check_binary()

        return self.children[1]

    @right.setter
    def right(self, value):
        self._check_binary()

        self.children[1] = value

    def __eq__(self, other):
        '''
        >>> Node(1, 2, 3) == Node(1, 2, 3)
        True
        >>> Node(1, 2, 3) != Node(1, 2, 3)
        False

        '''
        if self is other:
            return true

        if self.value != other.value:
            return false

        return self.children == other.children

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self, level=0):
        '''Pretty-printing

        >>> Node(1, 2, 3)
        Node(1,
          2,
          3)

        #>>> Node(5, Node(4, Node(2), Node(3)), Node(6))
        Node(5,
          Node(4,
            Node(2),
            Node(3)),
          Node(6))

        '''
        indent = '  ' * level

        result = indent + 'Node({}'.format(repr(self.value))
        if len(self.children) > 0:
            result += ','

        for i, c in enumerate(self.children):
            try:
                rep = c.__repr__(level = level + 1)
            except TypeError:
                rep = indent + '  ' + repr(c)

            result += indent + '\n{}'.format(rep)
            if i != len(self.children) - 1:
                result += ','

        return result + ')'

    def rotateLeft(self):
        '''
        >>> n = Node('P', 'A', Node('Q', 'B', 'C'))
        >>> n.rotateLeft() == Node('Q', Node('P', 'A', 'B'), 'C')
        True

        '''
        if not isinstance(self.right, Node):
            return False

        right = self.right
        self.right = right.left

        right.left = self
        return right

    def rotateRight(self):
        '''
        >>> n = Node('Q', Node('P', 'A', 'B'), 'C')
        >>> n.rotateRight() == Node('P', 'A', Node('Q', 'B', 'C'))
        True

        '''
        if not isinstance(self.left, Node):
            return False

        left = self.left
        self.left = left.right

        left.right = self
        return left

if __name__ == '__main__':
    import doctest
    doctest.testmod()
