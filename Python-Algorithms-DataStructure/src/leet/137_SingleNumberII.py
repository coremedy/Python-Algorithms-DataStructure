'''
Created on 2015-10-30
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :       1st    2nd     3rd
        : x  ^  A    ^ A     ^ 0    = x
        : y  ^  0      A       A    = y
        : self-reflection of xor
        """
        x, y = 0, 0
        for n in nums:
            x ^= (~y) & n
            y ^= (~x) & n
        return x

if __name__ == '__main__':
    pass