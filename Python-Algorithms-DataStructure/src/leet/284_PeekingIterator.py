'''
Created on 2015-11-03
'''

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.e, self.iterator = None, iterator
        self.fetch()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.e:
            return self.e

    def next(self):
        """
        :rtype: int
        """
        if not self.e:
            self.fetch()
        if self.e:
            val = self.e
            self.fetch()
            return val
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.e:
            return True
        else:
            self.fetch()
            return True if self.e else False
            
    def fetch(self):
        self.e = self.iterator.next() if self.iterator.hasNext() else None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
if __name__ == '__main__':
    pass