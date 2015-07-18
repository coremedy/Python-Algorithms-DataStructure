'''
Created on 2015-07-18
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        max_record = [nums[0]]
        min_record = [nums[0]]
        for index in range(1, len(nums)):
            if nums[index] == 0:
                max_record.append(0)
                min_record.append(0)
            elif nums[index] > 0:
                max_record.append(max(nums[index], nums[index] * max_record[index - 1]))
                min_record.append(min(nums[index], nums[index] * min_record[index - 1]))
            else:
                max_record.append(max(nums[index], nums[index] * min_record[index - 1]))
                min_record.append(min(nums[index], nums[index] * max_record[index - 1]))
        return max(max_record)

if __name__ == '__main__':
    pass