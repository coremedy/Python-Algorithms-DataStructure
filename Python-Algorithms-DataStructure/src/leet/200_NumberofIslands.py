'''
Created on 2015-08-01
'''

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        result = 0
        row_length = len(grid)
        if row_length == 0:
            return result
        col_length = len(grid[0])
        if col_length == 0:
            return result
        recorder = [[False for dummy_col in range(col_length)] for dummy_row in range(row_length)]
        neighbours = zip([0, 0, -1, 1], [-1, 1, 0, 0])
        # This problem is to calculate connected components
        for row in range(row_length):
            for col in range(col_length):
                if not recorder[row][col] and grid[row][col] == '1':
                    self.DFS(row, col, grid, recorder, neighbours, row_length, col_length)
                    result += 1
        return result
    
    def DFS(self, row, col, grid, recorder, neighbours, row_length, col_length):
        recorder[row][col] = True
        for row_inc, col_inc in neighbours:
            row_new = row + row_inc
            col_new = col + col_inc
            if row_new >= 0 and row_new < row_length and col_new >= 0 and col_new < col_length and not recorder[row_new][col_new] and grid[row_new][col_new] == '1':
                self.DFS(row_new, col_new, grid, recorder, neighbours, row_length, col_length)

if __name__ == '__main__':
    pass