'''
Created on 2015-08-30
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        d = {s[0] : 0}
        beg, end, result = 0, 0, 0
        for index in range(1, len(s)):
            beg, d[s[index]], end, result = beg if s[index] not in d or (s[index] in d and d[s[index]] < beg) else d[s[index]] + 1, index, index, max(result, end - beg + 1)
        result = max(result, end - beg + 1)
        return result

if __name__ == '__main__':
    pass