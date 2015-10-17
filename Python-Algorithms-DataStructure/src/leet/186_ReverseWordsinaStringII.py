'''
Created on 2015-10-17
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        beg = 0
        for index in range(len(s)):
            if s[index] == ' ':
                self.reverseWord(s, beg, index - 1)
                beg = index + 1
        self.reverseWord(s, beg, len(s) - 1)
        self.reverseWord(s, 0, len(s) - 1)

    def reverseWord(self, s, beg, end):
        while beg < end:
            s[beg], s[end], beg, end = s[end], s[beg], beg + 1, end - 1

if __name__ == '__main__':
    pass