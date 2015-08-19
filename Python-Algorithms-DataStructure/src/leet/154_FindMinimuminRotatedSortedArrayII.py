'''
Created on 2015-08-19
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        beg = 0
        end = len(nums) - 1
        while end - beg > 1:
            while beg < end and nums[beg] == nums[beg + 1]:
                beg += 1
            if end - beg == 1:
                break
            while beg < end and nums[end] == nums[end - 1]:
                end -= 1
            if end - beg == 1:
                break
            mid = (beg + end) // 2
            if nums[beg] <= nums[mid]:
                beg = mid
            else:
                end = mid
        return min(nums[0], nums[beg], nums[end], nums[-1])

if __name__ == '__main__':
    pass