'''
Created on 2015-08-29
less than a non-negative number, n
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        mark = [True] * n
        mark[0], mark[1] = False, False
        i = 2
        while i * i < n:
            if mark[i]:
                for j in range(i * i, n, i):
                    mark[j] = False
            i += 1
        return sum(mark)

if __name__ == '__main__':
    pass