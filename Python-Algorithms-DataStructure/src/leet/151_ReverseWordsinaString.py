'''
Created on 2015-10-15
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))

if __name__ == '__main__':
    pass