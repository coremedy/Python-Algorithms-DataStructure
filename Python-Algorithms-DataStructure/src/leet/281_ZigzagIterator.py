'''
Created on 2015-11-03
'''

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v, self.row, self.col = [v1, v2], 1, -1

    def next(self):
        """
        :rtype: int
        """
        return self.v[self.row][self.col]

    def hasNext(self):
        """
        :rtype: bool
        """
        count = 2
        while count > 0:
            self.row = (self.row + 1) % 2
            self.col = self.col + 1 if not self.row else self.col
            if self.col < len(self.v[self.row]):
                return True
            count -= 1
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    pass