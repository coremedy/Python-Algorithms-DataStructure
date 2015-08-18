'''
Created on 2015-08-18
'''

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        result, total, beg = 0, 0, 0
        for index in range(len(nums)):
            total += nums[index]
            while total - nums[beg] >= s:
                total -= nums[beg]
                beg += 1
            if total >= s:
                result = (index - beg + 1) if result == 0 else min(result, index - beg + 1)
        return result

if __name__ == '__main__':
    pass