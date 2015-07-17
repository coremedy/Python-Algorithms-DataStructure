'''
Created on 2015-07-16
'''

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row_len = len(grid)
        if row_len == 0:
            return 0
        col_len = len(grid[0])
        if col_len == 0:
            return 0
        if row_len == 1 and col_len == 1:
            return grid[0][0]
        else:
            for row in range(0, row_len):
                for col in range(0, col_len):
                    val = grid[row][col]
                    if row == 0 and col == 0:
                        pass
                    elif row == 0:
                        grid[row][col] += grid[row][col - 1]
                    elif col == 0:
                        grid[row][col] += grid[row - 1][col]
                    else:
                        grid[row][col] = min(val + grid[row][col - 1], val + grid[row - 1][col])
            return grid[row_len - 1][col_len - 1]

if __name__ == '__main__':
    pass