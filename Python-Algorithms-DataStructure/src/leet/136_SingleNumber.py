'''
Created on 2015-08-31
XOR
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in nums:
            result ^= n
        return result

if __name__ == '__main__':
    pass