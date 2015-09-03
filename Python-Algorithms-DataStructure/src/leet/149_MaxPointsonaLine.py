'''
Created on 2015-09-03
Sub-problem should be points, not lines
'''

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 1:
            return len(points)
        result = 0
        for index1 in range(len(points) - 1):
            pt1, d, same, local_max = points[index1], {None : 0}, 1, 0
            # Start from the next one because
            # we dont need to calculate the prev once more
            for index2 in range(index1 + 1, len(points)):
                pt2 = points[index2]
                if pt1.x == pt2.x and pt1.y != pt2.y:
                    d[None] += 1
                    local_max = max(local_max, d[None])
                elif pt1.x != pt2.x:
                    a = float(pt2.y - pt1.y) / float(pt2.x - pt1.x)
                    if a not in d:
                        d[a] = 0
                    d[a] += 1
                    local_max = max(local_max, d[a])
                else:
                    same += 1
            result = max(result, local_max + same)
        return result

if __name__ == '__main__':
    pass