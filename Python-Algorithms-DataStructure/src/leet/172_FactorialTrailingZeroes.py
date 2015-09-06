'''
Created on 2015-09-06
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        :http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/ 
        """
        result, base = 0, 5
        while n / base >= 1:
            result, base = result + (n // base), base * 5
        return result

if __name__ == '__main__':
    pass