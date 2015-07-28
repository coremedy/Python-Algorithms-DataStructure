'''
Created on 2015-07-28
'''

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()']
        result = []
        self.BackTrack('()', 0, 1, n, result)
        return result
        
    def BackTrack(self, s, start, depth, n, result):
        if depth == n:
            result.append(s)
        else:
            for index in range(start, len(s)):
                self.BackTrack(s[:index + 1] + '()' + s[index + 1:], index + 1, depth + 1, n, result)

if __name__ == '__main__':
    pass