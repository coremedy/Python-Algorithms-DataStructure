'''
Created on 2015-10-11
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Baseline
        if n == 0:
            return 1.0
        positive, n = True if n > 0 else False, abs(n)
        if x == 0.0 or x == 1.0:
            return x
        if x == -1.0:
            return -x if n % 2 == 0 else x
        cache = {0 : 1.0, 1 : x}
        result = self.pow_rec(x, n, cache)
        return result if positive else 1 / result
    
    def pow_rec(self, x, n, cache):
        if n in cache:
            return cache[n]
        half_n = n // 2
        cache[half_n] = self.pow_rec(x, half_n, cache)
        cache[n] = cache[half_n] * cache[half_n] * (1.0 if n % 2 == 0 else x)
        return cache[n]

if __name__ == '__main__':
    pass