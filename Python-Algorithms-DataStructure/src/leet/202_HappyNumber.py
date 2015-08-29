'''
Created on 2015-08-29
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n, tmp = 0, n
            while tmp != 0:
                n, tmp = n + (tmp % 10) * (tmp % 10), tmp // 10
        return True if n == 1 else False

if __name__ == '__main__':
    pass