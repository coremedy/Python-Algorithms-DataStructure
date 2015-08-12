'''
Created on 2015-08-12
'''

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if len(nums) > 0:
            begin = 0
            end = len(nums) - 1
            index = 0
            while index <= end:
                if nums[index] == 0:
                    nums[begin], nums[index] = nums[index], nums[begin]
                    begin += 1
                    # Should be 1
                    index += 1
                elif nums[index] == 2:
                    nums[index], nums[end] = nums[end], nums[index]
                    end -= 1
                    # Check the current
                else:
                    index += 1

if __name__ == '__main__':
    pass