'''
Created on 2015-07-21
'''

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        s1_length = len(s1)
        s2_length = len(s2)
        s3_length = len(s3)
        if s3_length != s1_length + s2_length:
            return False
        if s1_length == 0 and s2 != s3:
            return False
        if s2_length == 0 and s1 != s3:
            return False
        table = [[True for dummy_col in range(s1_length + 1)] for dummy_row in range(s2_length + 1)]
        for row in range(s2_length + 1):
            for col in range(s1_length + 1):
                if row and col:
                    table[row][col] = (table[row - 1][col] and (s2[row - 1] == s3[row + col - 1])) or (table[row][col - 1] and (s1[col - 1] == s3[row + col - 1]))
                elif row and not col:
                    table[row][col] = table[row - 1][col] and (s2[row - 1] == s3[row + col - 1])
                elif not row and col:
                    table[row][col] = table[row][col - 1] and (s1[col - 1] == s3[row + col - 1])
        return table[s2_length][s1_length]

if __name__ == '__main__':
    pass