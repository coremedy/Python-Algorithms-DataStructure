'''
Created on 2015-10-10
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        d = { 0 : 0, 1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 1, 8 : 1, 9 : 1 }
        if n < 10:
            return d[n]
        k, lst = 100, n % 10
        while True:
            cur = n % k
            if cur not in d:
                sig_digit, count = cur // (k // 10), 0
                if sig_digit > 1:
                    cur, count = cur - lst - 1, count + d[lst]
                    sig_digit = cur // (k // 10)
                    if sig_digit > 1:
                        count, cur = count + (sig_digit - 1) * d[(k // 10) - 1], (k // 10) * 2 - 1
                count += d[cur % (k // 10)] + d[(k // 10) - 1] + cur % (k // 10) + 1
                d[n % k] = count
            if n == n % k:
                break 
            d[k - 1], k, lst = 10 * d[(k - 1) % (k // 10)] + (k - 1) % (k // 10) + 1, k * 10, n % k
        return d[n]

if __name__ == '__main__':
    pass