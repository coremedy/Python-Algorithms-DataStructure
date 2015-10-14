'''
Created on 2015-10-14
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for ch in reversed(s.rstrip(' ')):
            if ch.isalpha():
                result += 1
            else:
                break
        return result

if __name__ == '__main__':
    pass