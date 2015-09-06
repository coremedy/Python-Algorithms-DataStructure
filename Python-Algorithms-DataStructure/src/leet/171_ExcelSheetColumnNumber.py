'''
Created on 2015-09-06
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, base = 0, 1
        for ch in reversed(s):
            result, base = result + (ord(ch) - 0x40) * base, base * 26
        return result

if __name__ == '__main__':
    pass