'''
Created on 2015-07-18

Eg, A - B - C - D - E - A, E is the new element
MAX_VALUE_CYCLE[A-E cycle] = max(MAX_VALUE_WITHOUT_CYCLE[A-D without cycle], NUMS[E] + MAX_VALUE_WITHOUT_CYCLE[B-C])
                                 No E here                                   E is here, then A and D should not be here
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        houses_length = len(nums)
        if houses_length == 0:
            return 0
        elif houses_length <= 3:
            return max(nums)
        else:
            return max(self.rob_without_cycle(nums[:houses_length - 1]), nums[houses_length - 1] + self.rob_without_cycle(nums[1 : houses_length - 2]))
    
    def rob_without_cycle(self, nums):
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