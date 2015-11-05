'''
Created on 2015-11-05
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums):
            prev = -1
            for index in range(len(nums)):
                if not nums[index] and prev < 0:
                    prev = index
                elif nums[index] and prev >= 0:
                    nums[prev] = nums[index]
                    prev += 1
            if prev > 0:
                for index in range(prev, len(nums)):
                    nums[index] = 0

if __name__ == '__main__':
    pass