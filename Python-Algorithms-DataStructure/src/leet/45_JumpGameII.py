'''
Created on 2015-08-19
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        result = 0
        beg = 0
        bound = beg + nums[beg]
        while True:
            if bound >= len(nums) - 1:
                return result + 1
            local_max = bound
            locaL_best = beg
            for index in range(beg + 1, bound + 1):
                if index + nums[index] > local_max:
                    local_max = index + nums[index]
                    locaL_best = index
            if locaL_best == beg:
                return 0
            result += 1
            beg, bound = bound, local_max

if __name__ == '__main__':
    pass