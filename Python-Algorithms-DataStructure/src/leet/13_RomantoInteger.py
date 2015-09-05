'''
Created on 2015-09-05
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, result, prev = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}, 0, ''
        for ch in s:
            if prev == '':
                prev = ch
            elif d[prev] >= d[ch]:
                result += d[prev]
                prev = ch
            elif d[prev] < d[ch]:
                result += d[ch] - d[prev]
                prev = ''
        if prev != '':
            result += d[prev]
        return result

if __name__ == '__main__':
    pass