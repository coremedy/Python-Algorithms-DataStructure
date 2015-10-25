'''
Created on 2015-10-25
'''

import heapq

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        heap = []
        heapq.heapify(heap)
        for i in sorted(intervals, key = lambda x: (x.start, x.end)):
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        return len(heap)

if __name__ == '__main__':
    pass