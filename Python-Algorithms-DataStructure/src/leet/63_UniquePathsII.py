'''
Created on 2015-07-18
'''

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for dummy_col in range(0, n + 1)] for dummy_row in range(0, m + 1)]
        if obstacleGrid[0][0] == 0:
            table[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if not (row == 1 and col == 1):
                    if obstacleGrid[row - 1][col - 1]:
                        table[row][col] = 0
                    else:
                        if (obstacleGrid[row - 2][col - 1] == 1) and (obstacleGrid[row - 1][col - 2] == 1):
                            table[row][col] = 0
                        elif obstacleGrid[row - 2][col - 1] == 1:
                            table[row][col] = table[row][col - 1]
                        elif obstacleGrid[row - 1][col - 2] == 1:
                            table[row][col] = table[row - 1][col]
                        else:
                            table[row][col] = table[row][col - 1] + table[row - 1][col]
        return table[m][n]

if __name__ == '__main__':
    pass