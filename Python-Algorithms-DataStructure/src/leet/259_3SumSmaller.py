'''
Created on 2015-08-18
The problem asks you to return count, not actual value
If actual value is required, the complexity will increase to O(n^3)
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        if len(nums) < 3:
            return 0
        nums.sort()
        result = 0
        for index_first in range(len(nums) - 2):
            index_second = index_first + 1
            index_third = len(nums) - 1
            while index_second < index_third:
                if nums[index_first] + nums[index_second] + nums[index_third] >= target:
                    index_third -= 1
                else:
                    # if nums[index_first] + nums[index_second] + nums[index_third] < target
                    # nums[index_first] + nums[index_second] + nums[index_second + 1, index_third - 1] also < target
                    result += index_third - index_second
                    index_second += 1
        return result

if __name__ == '__main__':
    pass