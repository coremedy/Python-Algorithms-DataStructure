'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        last_elem = nums[0]
        for index in range(1, len(nums)):
            if nums[index] > last_elem:
                last_elem = nums[index]
            else:
                return nums[index]
        return nums[0]

if __name__ == '__main__':
    pass