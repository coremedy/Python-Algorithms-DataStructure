'''
Created on 2015-08-16
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        prev = nums[0]
        local_count = 1
        result = 0
        for index in range(1, len(nums)):
            if nums[index] == prev:
                local_count += 1
            else:
                nums[result] = prev
                result += 1
                if local_count > 1:
                    nums[result] = prev
                    result += 1
                prev = nums[index]
                local_count = 1
        nums[result] = prev
        result += 1
        if local_count > 1:
            nums[result] = prev
            result += 1
        return result

if __name__ == '__main__':
    pass