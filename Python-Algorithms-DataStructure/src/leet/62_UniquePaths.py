'''
Created on 2015-07-17
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        table = [[0 for dummy_col in range(0, n + 1)] for dummy_row in range(0, m + 1)]
        table[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if not (row == 1 and col == 1):
                    table[row][col] = table[row][col - 1] + table[row - 1][col]
        return table[m][n]

if __name__ == '__main__':
    pass