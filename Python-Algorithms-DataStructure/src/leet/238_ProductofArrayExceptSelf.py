'''
Created on 2015-08-16
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if len(nums) < 2:
            return 1
        result = [1]
        for index in range(len(nums) - 1):
            result.append(result[-1] * nums[index])
        elem = nums[-1]
        nums[-1] = 1
        for index in range(len(nums) - 2, -1, -1):
            nums[index], elem = nums[index + 1] * elem, nums[index]
        for index in range(len(nums)):
            result[index] *= nums[index]
        return result

if __name__ == '__main__':
    pass