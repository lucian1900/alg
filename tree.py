#!/usr/bin/env python

class Node(object):
    def __init__(self, value, *children):
        self.value = value
        self.children = children

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

        self.children[0] = value

    def __repr__(self, level=0):
        '''Pretty-printing

        >>> Node(1, 2, 3)
        Node(1,
          2,
          3)
        '''
        indent = '  ' * level

        result = indent + 'Node({},'.format(self.value)

        for i, c in enumerate(self.children):
            try:
                rep = c.__repr__(level = level + 1)
            except TypeError:
                rep = indent + '  ' + repr(c)

            result += indent + '\n{}'.format(rep)
            if i != len(self.children) - 1:
                result += ','

        return result + ')'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
