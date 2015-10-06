'''
Created on 2015-10-06
10000 & (01111) = 0
10000 minus 1 = 01111
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n & (n - 1)) == 0 if n > 0 else False

if __name__ == '__main__':
    pass