'''
Created on 2015-09-01
'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len <= 2:
            return s_len
        result, beg, index, ch1, ch2, ch1_pos, ch2_pos = 0, 0, 0, '', '', -1, -1
        for ch in s:
            if ch == ch1:
                ch1, ch1_pos, ch2, ch2_pos = ch2, ch2_pos, ch, index
            elif ch != ch2:
                ch1, ch1_pos, ch2, ch2_pos, beg = ch2, ch2_pos, ch, index, ch2_pos if ch2_pos != -1 else 0
            index, result = index + 1, max(result, index - beg + 1)
        return result

if __name__ == '__main__':
    pass