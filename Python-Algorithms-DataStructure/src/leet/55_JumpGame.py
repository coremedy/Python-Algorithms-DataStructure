'''
Created on 2015-08-15
'''

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if len(nums) <= 1:
            return True
        vaild_until = nums[0]
        index = 0
        while True:
            if vaild_until >= len(nums) - 1:
                return True
            if index + nums[index] > vaild_until:
                vaild_until = index + nums[index]
            else:
                if index == vaild_until:
                    return False
            index += 1

if __name__ == '__main__':
    pass