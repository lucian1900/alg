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
                i = i.find(value)

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


class AVLNode(object):
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    @property
    def balance(self):
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0

        return left - right

    @property
    def height(self):
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0

        return 1 + max(left, right)

    def rotate_left(self):
        self.data, self.right.data = self.right.data, self.data

        old_left = self.left
        self.left, self.right = self.right, self.right.right

        self.left.left, self.left.right = old_left, self.left.left

    def rotate_right(self):
        self.data, self.left.data = self.left.data, self.data

        old_right = self.right
        self.left, self.right = self.leftl.left, self.left
        self.right.left, self.right.left = self.right.right, old_right

    def rotate_left_right(self):
        self.left.rotate_left()
        self.rotate_right()

    def rotate_right_left(self):
        self.right.rotate_right()
        self.rotate_left()

    def rebalance(self):
        bal = self.balance
        if bal > 1:
            if self.left.balance > 0:
                self.rotate_right()
            else:
                self.rotate_left_right()
        elif bal < -1:
            if self.right.balance < 0:
                self.rotate_left()
            else:
                self.rotate_right_left()


    def insert(self, data):
        if data <= self.data:
            if not self.left:
                self.left = AVLNode(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = AVLNode(data)
            else:
                self.right.insert(data)

        self.rebalance()

    def ___str___(self, indent = 0):
        result = " " * indent + str(self.data)

        if self.left:
            result += self.left.__str__(indent + 2)
        if self.right:
            result += self.right.__str__(indent + 2)

        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
