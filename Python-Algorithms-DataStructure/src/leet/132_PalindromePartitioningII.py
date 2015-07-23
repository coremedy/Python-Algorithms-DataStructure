'''
Created on 2015-07-22
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        s_length = len(s)
        if s_length == 0 or s_length == 1:
            return 0
        palindrome_state = [[False for dummy_col in range(s_length)] for dummy_row in range(s_length)]
        # DP for palindrome state
        for row in range(s_length - 1, -1, -1):
            for col in range(s_length - 1, row - 1, -1):
                if col - row == 0:
                    palindrome_state[row][col] = True
                elif col - row == 1:
                    palindrome_state[row][col] = (s[row] == s[col])
                else:
                    palindrome_state[row][col] = (palindrome_state[row + 1][col - 1]) and (s[row] == s[col])
        # DP for min cut
        table = [row for row in range(s_length)]
        for col in range(s_length):
            if palindrome_state[0][col]:
                table[col] = 0
            else:
                for prev_col in range(col - 1, -1, -1):
                    if palindrome_state[prev_col + 1][col]:
                        table[col] = min(table[col], table[prev_col] + 1)
        return table[s_length - 1]

if __name__ == '__main__':
    pass