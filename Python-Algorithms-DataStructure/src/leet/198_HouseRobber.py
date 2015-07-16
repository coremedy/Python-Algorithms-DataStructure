'''
Created on 2015-07-16
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        length_of_nums = len(nums)
        if length_of_nums == 0:
            return 0
        elif length_of_nums == 1:
            return nums[0]
        elif length_of_nums == 2:
            return max(nums)
        else:
            result = [0 for dummy_i in range(0, length_of_nums)]
            result[0] = nums[0]
            result[1] = max(nums[0], nums[1])
            for index in range(2, length_of_nums):
                result[index] = max(result[index - 1], nums[index] + result[index - 2])
            return result[length_of_nums - 1]

if __name__ == '__main__':
    pass