'''
Created on 2015-10-18
This problem tests the knowledge of next array in KMP algorithm
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        # To avoid such condition we need to add @ here:
        # "aabba" -> aabbaabbaa
        # aabbaabbaa
        # 0100123456
        # That is:
        # aabbaa
        #     aabbaa
        pattern = s + '@' + s[::-1]
        p = [0 for dummy_i in range(len(pattern))]
        for i in range(1, len(pattern)):
            j = p[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                # abakabad
                # ---X---X
                # Then the range goes to aba
                # abakabad
                # -X    -X
                # Then the range goes to a
                # abakabad
                # X      X
                j = p[j - 1]
            p[i] = j + (1 if pattern[j] == pattern[i] else 0)
        return s[len(s) - 1: p[-1] - 1: - 1] + s

if __name__ == '__main__':
    pass