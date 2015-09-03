'''
Created on 2015-09-03
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n != 0:
            r = n % 26 if n % 26 != 0 else 26
            result.append(chr(r + 64))
            n = (n - r) // 26
        return ''.join(reversed(result))

if __name__ == '__main__':
    pass