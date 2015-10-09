'''
Created on 2015-10-09
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (1 + len(nums)) // 2 - sum(nums)
    
    # A XOR B = C => C XOR A = B
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for index in range(len(nums)):
            result ^= (index + 1) ^ nums[index]
        return result

if __name__ == '__main__':
    pass