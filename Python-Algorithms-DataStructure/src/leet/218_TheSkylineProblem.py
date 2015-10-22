'''
Created on 2015-10-22
'''

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        else:
            return self.divideAndMerge(buildings)
    
    def divideAndMerge(self, buildings):
        buildings_len = len(buildings)
        if buildings_len == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        else:
            return self.mergeSkyline(self.divideAndMerge(buildings[:buildings_len // 2]), self.divideAndMerge(buildings[buildings_len // 2:]))
        
    def mergeSkyline(self, s1, s2):
        s1_index, s1_len, s1_height, s2_index, s2_len, s2_height, result = 0, len(s1), 0, 0, len(s2), 0, []
        # if s1.x < s2.x
        # the current height of s2 will be s2_height
        # the result height should be max(s1.y, s2_height)
        # When will s1_height/s2_height be updated? - When we meet with a new point from s1/s2
        # Same principle applies for s1.x > s2.x and s1.x == s2.x
        while s1_index < s1_len and s2_index < s2_len:
            x, s1_height, s2_height = s1[s1_index][0] if s1[s1_index][0] <= s2[s2_index][0] else s2[s2_index][0], s1[s1_index][1] if s1[s1_index][0] <= s2[s2_index][0] else s1_height, s2[s2_index][1] if s2[s2_index][0] <= s1[s1_index][0] else s2_height
            h = max(s2_height, s1_height)
            s1_index, s2_index = (s1_index + 1) if s1[s1_index][0] <= s2[s2_index][0] else s1_index, (s2_index + 1) if s2[s2_index][0] <= s1[s1_index][0] else s2_index
            # Eliminate dup height (required by the problem desc)
            if len(result) == 0 or (len(result) > 0 and result[-1][1] != h):
                result.append([x, h])
        while s1_index < s1_len:
            result.append(s1[s1_index])
            s1_index += 1
        while s2_index < s2_len:
            result.append(s2[s2_index])
            s2_index += 1
        return result

if __name__ == '__main__':
    pass