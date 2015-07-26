'''
Created on 2015-07-26
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        result = []
        self.BackTrack(nums, result, [])
        return result
    
    def BackTrack(self, nums, result, cache):
        if len(nums) == 0:
            result.append(cache)
        else:
            for index in range(0, len(nums)):
                # This can be quicker
                self.BackTrack(nums[:index] + nums[index + 1:], result, cache + [nums[index]])

if __name__ == '__main__':
    pass