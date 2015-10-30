'''
Created on 2015-10-29
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        result = m & n
        for b in [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]:
            result = (result ^ b) if (result & b) and ((b + m <= n) or (n & b == 0)) else result
        return result
    
if __name__ == '__main__':
    pass