'''
Created on 2015-11-04
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        table = [nums[0]]
        for index in range(1, len(nums)):
            if nums[index] < table[0]:
                table[0] = nums[index]
            elif nums[index] > table[-1]:
                table.append(nums[index])
            else:
                table[self.binarySearch(0, len(table) - 1, table, nums[index])] = nums[index]
        return len(table)
        
    def binarySearch(self, beg, end, table, target):
        mid = (beg + end) // 2
        while beg < mid:
            if target == table[mid]:
                return mid
            elif target < table[mid]:
                end = mid
            else:
                beg = mid
            mid = (beg + end) // 2        
        return end if table[end] == target else (mid if table[mid] == target else mid + 1)

if __name__ == '__main__':
    pass