'''
Created on 2015-08-19
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        result = []
        for i in sorted(intervals, key=lambda x: (x.start, x.end)):
            if len(result) == 0 or i.start > result[-1].end:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
        return result

if __name__ == '__main__':
    pass