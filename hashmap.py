#!/usr/bin/env python

from collections import Mapping

class HashMap(Mapping):
    '''For educational purposes. Similar to CPython's dict in design.

    Tests
    >>> hm = HashMap()
    >>> hm[1] = 2
    >>> hm._array
    [None, (1, 2), None, None, None, None, None, None]

    >>> hm[1]
    2

    >>> hm['hello'] = 'world'
    >>> hm._array
    [None, (1, 2), None, None, None, ('hello', 'world'), None, None]

    >>> h = HashMap([(1, 2), ('hello', 'world')])
    >>> h._array
    [None, (1, 2), None, None, None, ('hello', 'world'), None, None]

    '''
    def __init__(self, mapping=[]):
        self._pow2 = 3
        self._length = 2 ** self._pow2
        self._array = [None] * self._length

        self.update(mapping)

    def update(self, mapping):
        try:
            mapping = mapping.items()
        except AttributeError:
            pass

        for k, v in mapping:
            self[k] = v

    def items(self):
        mapping = []
        for i in self._array:
            if i: mapping.append(i)

    def __getitem__(self, key):
        h = hash(key)
        for i in xrange(self._length):
            item = self._array[h % self._length]

            if isinstance(item, tuple):
                k, v = item
                if k == key:
                    return v

            h >>= self._pow2
            h += 1 # touch the entire array

        raise KeyError("No such key: {}".format(key))

    def __setitem__(self, key, value):
        h = hash(key)
        for i in xrange(self._length):
            index = h % self._length
            item = self._array[index]

            if not item:
                self._array[index] = (key, value)
                break

            h >>= self._pow2
            h += 1

    def __delitem__(self, key):
        h = hash(key)
        for i in xrange(self._length):
            index = h % self._length
            item = self._array[index]

            if isinstance(item, tuple):
                k, v = item
                if k == key:
                    self._array[index] = True #dummy value
                    return

            h >>= self._pow2
            h += 1

    def __iter__(self):
        return iter(self._array)

    def __len__(self):
        return len(self._array)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
