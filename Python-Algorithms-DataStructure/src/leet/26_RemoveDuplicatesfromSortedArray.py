'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        end = 0
        # Don't need to use del. Just swap and swap ...
        for i in range(1, len(nums)):
            if nums[i] != nums[end]:
                end += 1
                nums[i], nums[end] = nums[end], nums[i]
        return end + 1

if __name__ == '__main__':
    pass