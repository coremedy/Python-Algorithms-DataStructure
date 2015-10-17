'''
Created on 2015-10-17
A little bit better than O(n^2). Brute-Force search from mid to lef/right
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_len, beg, end = 1, 0, 0
        for index in range(len(s) - 1):
            count = 1
            if s[index] != s[index + 1]:
                while index - count >= 0 and index + count < len(s) and s[index - count] == s[index + count]:
                    count += 1
                if (count - 1) * 2 + 1 > max_len:
                    max_len, beg, end = (count - 1) * 2 + 1, index - (count - 1), index + (count - 1)
            else:
                repetition = 1
                while index + 1 < len(s) and s[index] == s[index + 1]:
                    index, repetition = index + 1, repetition + 1
                while index - (repetition - 1) - count >= 0 and index + count < len(s) and s[index - (repetition - 1) - count] == s[index + count]:
                    count += 1
                if (count - 1) * 2 + repetition > max_len:
                    max_len, beg, end = (count - 1) * 2 + repetition, index - (repetition - 1) - (count - 1), index + count - 1
        return s[beg : end + 1]

if __name__ == '__main__':
    pass