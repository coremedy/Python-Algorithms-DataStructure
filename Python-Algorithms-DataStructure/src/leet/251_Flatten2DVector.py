'''
Created on 2015-11-02
'''

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row, self.vec2d = 0, vec2d
        self.findNext(0)        

    def next(self):
        """
        :rtype: int
        """
        if self.row < len(self.vec2d):
            val = self.vec2d[self.row][self.col]
            if self.col + 1 < len(self.vec2d[self.row]):
                self.col += 1
            else:
                self.findNext(self.row + 1)
            return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.row < len(self.vec2d)
        
    def findNext(self, start):
        self.row = start
        while self.row < len(self.vec2d):
            if self.vec2d[self.row]:
                break
            self.row += 1
        if self.row < len(self.vec2d):
            self.col = 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    pass