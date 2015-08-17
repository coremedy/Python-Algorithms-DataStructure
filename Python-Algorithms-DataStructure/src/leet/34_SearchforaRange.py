'''
Created on 2015-08-17
Trivial solution. Performance is bad but this serves as a good demonstration of binary search
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        index = self.binary_search(nums, target)
        if index == -1:
            return [-1, -1]
        else:
            return [self.search_for_left_bound(nums, 0, index, target), self.search_for_right_bound(nums, index, len(nums) - 1, target)]
    
    def binary_search(self, nums, target):
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
        if nums[begin] == target:
            return begin
        else:
            return -1
            
    def search_for_left_bound(self, nums, begin, end, target):
        while begin != end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                end = mid
            else:
                begin = mid + 1
        return begin
    
    def search_for_right_bound(self, nums, begin, end, target):
        while begin != end:
            mid = (begin + end) // 2 + 1
            if nums[mid] == target:
                begin = mid
            else:
                end = mid - 1
        return begin  

if __name__ == '__main__':
    pass