'''
Created on 2015-10-29
'''

class Solution(object):
    def hammingWeight(self, i):
        """
        :type n: int
        :rtype: int
        : SWAR algorithm
        """
        i = i - ((i >> 1) & 0x55555555)
        i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
        return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

if __name__ == '__main__':
    pass