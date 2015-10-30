'''
Created on 2015-10-29
'''

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for index in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

if __name__ == '__main__':
    pass