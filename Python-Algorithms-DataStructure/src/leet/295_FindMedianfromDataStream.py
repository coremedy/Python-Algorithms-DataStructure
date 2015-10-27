'''
Created on 2015-10-27
'''

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap, self.max_heap, self.count = [], [], 0
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.count == 0 or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        self.count += 1
        left_count = self.count // 2
        if len(self.max_heap) > left_count:
            gap = len(self.max_heap) - left_count
            while gap > 0:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                gap -= 1
        elif len(self.max_heap) < left_count:
            gap = left_count - len(self.max_heap)
            while gap > 0:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                gap -= 1        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.count == 0:
            return 0.0
        if self.count % 2 == 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] * 1.0 - self.max_heap[0] * 1.0) / (2.0)        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == '__main__':
    pass