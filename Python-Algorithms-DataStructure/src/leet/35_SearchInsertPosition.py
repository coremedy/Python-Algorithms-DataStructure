'''
Created on 2015-08-15
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        begin = 0
        end = len(nums) - 1
        while begin != end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                begin = mid + 1
        if target <= nums[begin]:
            return begin
        else:
            return begin + 1

if __name__ == '__main__':
    pass