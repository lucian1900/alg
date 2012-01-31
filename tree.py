#!/usr/bin/env python

class Node(object):
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __repr__(self, level=0):
        '''Pretty-printing

        >>> Node(1, 2, 3)
        Node(1,
          2,
          3)
        '''
        indent = '  ' * level

        result = indent + 'Node({},'.format(self.value)

        for i in self.children:
            try:
                c = i.__repr__(level = level + 1)
            except TypeError:
                c = indent + '  ' + repr(i)

            result += indent + '\n  {}'.format(c)

        return result + ')'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
