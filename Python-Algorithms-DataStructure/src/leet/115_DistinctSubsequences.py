'''
Created on 2015-07-19

Something like Edit Distance 

'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        if len(s) < len(t):
            return 0
        table = [[0 for dummy_col in range(0, len(s) + 1)] for dummy_row in range(0, len(t) + 1)]
        # "" and S
        # Only one way to make them equal: remove all chars in S
        for col in range(len(s) + 1):
            table[0][col] = 1
        # DP start ...
        for row in range(1, len(t) + 1):
            for col in range(1, len(s) + 1):
                # Equal: 1. skip this char 2. do not skip and compare strings with this char removed
                if s[col - 1] == t[row - 1]:
                    table[row][col] = table[row][col - 1] + table[row - 1][col - 1]
                # Not equal, remove this char in S
                else:
                    table[row][col] = table[row][col - 1]
        return table[len(t)][len(s)]

if __name__ == '__main__':
    pass