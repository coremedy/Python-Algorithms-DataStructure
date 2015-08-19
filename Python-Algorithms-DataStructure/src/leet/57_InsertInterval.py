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
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        result = []
        hit = False
        for i in sorted(intervals, key=lambda x: (x.start, x.end)):
            if not hit:
                if not (newInterval.start > i.end):
                    if newInterval.end < i.start:
                        result.append(newInterval)
                    else:
                        i.start = min(i.start, newInterval.start)
                        i.end = max(i.end, newInterval.end)
                    hit = True
                result.append(i)
            else:
                if i.start > result[-1].end:
                    result.append(i)
                else:
                    result[-1].end = max(result[-1].end, i.end)
        if not hit:
            result.append(newInterval)
        return result

if __name__ == '__main__':
    pass