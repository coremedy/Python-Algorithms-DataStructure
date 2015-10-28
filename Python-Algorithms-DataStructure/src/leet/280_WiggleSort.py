'''
Created on 2015-10-28
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        s = True
        for index in range(1, len(nums) - 1):
            if (s and nums[index] < nums[-1]) or (not s and nums[index] > nums[-1]):
                    nums[index], nums[-1] = nums[-1], nums[index]
            s = not s

if __name__ == '__main__':
    pass