'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        result = []
        start = 0
        for index in range(1, len(nums)):
            if not (nums[index] - nums[start] == index - start):
                result.append(str(nums[start]) if index - start == 1 else str(nums[start]) + "->" + str(nums[index - 1]))
                start = index
        result.append(str(nums[start]) if start == len(nums) - 1 else str(nums[start]) + "->" + str(nums[-1]))
        return result

if __name__ == '__main__':
    pass