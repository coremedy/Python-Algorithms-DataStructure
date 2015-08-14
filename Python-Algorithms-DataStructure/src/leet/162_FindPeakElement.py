'''
Created on 2015-08-14
So ... basically you don't know how to write binary search routine. Remember this one, ok?
'''

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        begin = 0
        end = len(nums) - 1
        while begin != end:
            mid = (begin + end) // 2
            if nums[mid] < nums[mid + 1]:
                begin = mid + 1
            else:
                end = mid
        return begin

if __name__ == '__main__':
    pass