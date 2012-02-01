#!/usr/bin/env python

class Node(object):
    '''

    >>> b = Node(1, 2, 3)
    >>> b.children[0]
    2
    >>> b.children[1] = 4
    >>> b.children
    [2, 4]

    '''

    def __init__(self, value, *children):
        self.value = value
        self.children = list(children)

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




class BNode(Node):
    '''Binary search tree node

    >>> BNode(1, 2, 3).left
    2
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.children = [left, right]

    @property
    def left(self):
        return self.children[0]

    @left.setter
    def left(self, value):
        self.children[0] = value

    @property
    def right(self):
        return self.children[1]

    @right.setter
    def right(self, value):
        self.children[1] = value

    def find(self, value):
        if self.value == value:
            return self

        for i in self.children:
            if isinstance(i, BNode):
                if i.find(value) == value:
                    return i
            else:
                if i == value:
                    return i


    def insert(self, value):
        pass

    def rotateLeft(self):
        '''
        >>> n = BNode('P', 'A', BNode('Q', 'B', 'C'))
        >>> n.rotateLeft() == BNode('Q', BNode('P', 'A', 'B'), 'C')
        True

        '''
        if not isinstance(self.right, BNode):
            return False

        right = self.right
        self.right = right.left

        right.left = self
        return right

    def rotateRight(self):
        '''
        >>> n = BNode('Q', BNode('P', 'A', 'B'), 'C')
        >>> n.rotateRight() == BNode('P', 'A', BNode('Q', 'B', 'C'))
        True

        '''
        if not isinstance(self.left, BNode):
            return False

        left = self.left
        self.left = left.right

        left.right = self
        return left


class AVLNode(BNode):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
