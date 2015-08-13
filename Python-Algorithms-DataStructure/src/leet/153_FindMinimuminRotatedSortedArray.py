'''
Created on 2015-08-13
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) <= 2:
            return min(nums)
        return nums[self.find_rotation_point(nums)]
        
    def find_rotation_point(self, nums):
        begin = 0
        end = len(nums) - 1
        mid = (begin + end) // 2
        if nums[begin] < nums[mid] and nums[mid] < nums[end]:
            return begin
        while end - begin > 1:
            if nums[mid] > nums[begin]:
                begin = mid
            else:
                end = mid
            mid = (begin + end) // 2
        return end

if __name__ == '__main__':
    pass