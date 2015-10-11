'''
Created on 2015-10-11
Newton's method
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        val, last, eps = x * 1.0, None, 0.000000001
        while True:
            last, val = val, (val + x / val) / 2
            if abs(last - val) <= eps:
                break
        return int(val)

if __name__ == '__main__':
    pass