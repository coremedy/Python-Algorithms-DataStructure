'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        nums.sort()
        start_index, end_index = -1, -1
        for index in range(len(nums)):
            if start_index == -1 and nums[index] == val:
                start_index = index
            if start_index != -1 and nums[index] != val:
                end_index = index
                break
        if start_index != -1:
            if end_index == -1:
                end_index = len(nums)
            del nums[start_index:end_index]
        return len(nums)

if __name__ == '__main__':
    pass