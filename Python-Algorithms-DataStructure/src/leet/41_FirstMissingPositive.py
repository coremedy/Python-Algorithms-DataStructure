'''
Created on 2015-08-18
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}    
    def firstMissingPositive(self, nums):
        nums_length = len(nums)
        if nums_length == 0:
            return 1
        index = 0
        while index < nums_length:
            current_val, nums[index] = nums[index], None
            index += 1
            if current_val > 0 and current_val <= nums_length:
                if current_val - 1 <= index - 1:
                    nums[current_val - 1] = current_val
                else:
                    if nums[current_val - 1] != current_val:
                        nums[current_val - 1], nums[index - 1] = current_val, nums[current_val - 1]
                        index -= 1
        for index in range(nums_length):
            if nums[index] is None:
                return index + 1
        return nums_length + 1
    
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive_Raw(self, nums):
        if len(nums) == 0:
            return 1
        index = 0
        while index < len(nums):
            if nums[index] > len(nums) or nums[index] <= 0:
                nums[index] = None
                index += 1
            else:
                if nums[index] - 1 <= index:
                    if nums[nums[index] - 1] is None:
                        nums[nums[index] - 1] = nums[index]
                    if nums[index] - 1 != index:
                        nums[index] = None
                    index += 1
                else:
                    if nums[index] == nums[nums[index] - 1]:
                        nums[index] = None
                        index += 1
                    else:                    
                        tmp = nums[index]
                        nums[index] = nums[tmp - 1]
                        nums[tmp - 1] = tmp
        for index in range(len(nums)):
            if nums[index] is None:
                return index + 1
        return len(nums) + 1

if __name__ == '__main__':
    pass