'''
Created on 2015-10-22
'''

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        S, D = 0, k
        for i in range(2, n + 1):
            S, D = D, (S + D) * (k - 1)
        return S + D

if __name__ == '__main__':
    pass