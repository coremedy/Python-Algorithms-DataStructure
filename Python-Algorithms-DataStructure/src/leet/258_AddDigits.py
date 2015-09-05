'''
Created on 2015-09-05
N = abc
N % 9 = (a * 10^2 + b * 10^1 + c) % 9 = (a * 1 + b * 1 + c * 1) % 9 = digits(N) 
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num % 9 if num % 9 != 0 else 9)

if __name__ == '__main__':
    pass