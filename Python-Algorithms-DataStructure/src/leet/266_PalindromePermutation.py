'''
Created on 2015-08-30
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        d = dict()
        count = 0
        for ch in s:
            if ch not in d:
                d[ch] = 1
                count += 1
            else:
                d[ch] += 1
                count = count - 1 if d[ch] % 2 == 0 else count + 1
        return True if (len(s) % 2 == 0 and count == 0) or (len(s) % 2 == 1 and count == 1) else False

if __name__ == '__main__':
    pass