'''
Created on 2015-08-15
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            return [str(lower) + '->' + str(upper)]
        result = []
        if nums[0] - lower == 1:
            result.append(str(lower))
        elif nums[0] - lower > 1:
            result.append(str(lower) + '->' + str(nums[0] - 1))
        prev = None
        for n in nums:
            if prev is None:
                prev = n
            else:
                if n - prev > 1:
                    if n - prev == 2:
                        result.append(str(prev + 1))
                    else:
                        result.append(str(prev + 1) + '->' + str(n - 1))
                prev = n
        if upper - nums[-1] == 1:
            result.append(str(upper))
        elif upper - nums[-1] > 1:
            result.append(str(nums[-1] + 1) + '->' + str(upper))
        return result

if __name__ == '__main__':
    pass