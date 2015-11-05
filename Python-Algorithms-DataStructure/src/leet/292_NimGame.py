'''
Created on 2015-11-05
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)
        ''' TLE
        if n <= 3:
            return True
        cache, n = [True, True, True], n - 3
        while n > 0:
            cur = (not cache[0]) or (not cache[1]) or (not cache[2])
            cache[0], cache[1], cache[2], n = cache[1], cache[2], cur, n - 1
        return cache[-1]
        '''

if __name__ == '__main__':
    pass