class HashMap(object):
    def __init__(self):
        self._array = [0]*8
        self._length = 8
    
    def _find(self, key):
        return hash(key) % self._length

    def __getitem__(self, key):
        return self._array[self._find(key)]

    def __setitem__(self, key, value):
        self._array[self._find(key)] = value
