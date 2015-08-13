'''
Created on 2015-08-13
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        nums_length = len(nums)
        if nums_length == 0:
            return -1
        if nums_length == 1:
            return -1 if nums[0] != target else 0
        if nums_length == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1
        rotation_point = self.find_rotation_point(nums)
        if rotation_point == 0:
            return self.binary_search(nums, target, 0, nums_length - 1)
        else:
            return self.binary_search(nums, target, rotation_point, nums_length - 1) if target < nums[0] else self.binary_search(nums, target, 0, rotation_point - 1)
            
    def binary_search(self, nums, target, begin, end):
        mid = (begin + end) // 2
        while begin != mid:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                begin = mid
            mid = (begin + end) // 2
        if target == nums[begin]:
            return begin
        elif target == nums[end]:
            return end
        else:
            return -1

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