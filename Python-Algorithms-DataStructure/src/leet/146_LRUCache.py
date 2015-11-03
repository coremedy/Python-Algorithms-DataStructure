'''
Created on 2015-11-03
'''

import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d, self.capacity = collections.OrderedDict(), capacity
        
    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.d:
            return -1
        val = self.d[key]
        del self.d[key]
        self.d[key] = val
        return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.d:
            gap = len(self.d) - (self.capacity - 1)
            while gap > 0:
                self.d.popitem(last=False)
                gap -= 1
        else:
            del self.d[key]
        self.d[key] = value    


if __name__ == '__main__':
    pass