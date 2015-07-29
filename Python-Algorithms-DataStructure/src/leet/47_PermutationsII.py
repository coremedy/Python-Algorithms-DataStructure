'''
Created on 2015-07-29
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        nums_length = len(nums)
        if nums_length == 0:
            return []
        if nums_length == 1:
            return [nums]
        nums.sort()
        result = []
        self.BackTrack(nums, result, [])
        return result
        
    def BackTrack(self, nums, result, cache):
        if len(nums) == 0:
            result.append(cache)
            return
        current = nums[0]
        self.BackTrack(nums[1:], result, cache + [current])
        for index in range(1, len(nums)):
            if nums[index] != current:
                current = nums[index]
                self.BackTrack(nums[:index] + nums[index + 1:], result, cache + [current])

if __name__ == '__main__':
    pass