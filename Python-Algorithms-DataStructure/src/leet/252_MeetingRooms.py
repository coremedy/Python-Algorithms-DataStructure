'''
Created on 2015-10-25
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        prev = None
        for i in sorted(intervals, key = lambda x: (x.start, x.end)):
            if prev and i.start < prev.end:
                return False
            prev = i
        return True

if __name__ == '__main__':
    pass