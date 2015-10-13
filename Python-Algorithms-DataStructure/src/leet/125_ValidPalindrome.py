'''
Created on 2015-10-13
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ''.join(ch.lower() for ch in s if ch.isalnum())
        return t == t[::-1]

if __name__ == '__main__':
    print(int(''))