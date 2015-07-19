'''
Created on 2015-07-19

Tricky problem: This is not to find out sub-problems like max-rec(cell-n), max-rec(cell-n+1)
                First, on a row-basis, find out how many consecutive 1's for every cell (this is a DP)
                Second, for every cell, check the column it belongs to and calculate the max-rec that
                has the width of its number of consecutive 1's 
'''

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        result = 0
        row_length = len(matrix)
        if row_length == 0:
            return result
        col_length = len(matrix[0])
        table = [[0 for dummy_col in range(col_length)] for dummy_row in range(row_length)]
        for row in range(row_length):
            table[row][0] = int(matrix[row][0])
        for row in range(row_length):
            for col in range(1, col_length):
                if int(matrix[row][col]):
                    table[row][col] = table[row][col - 1] + 1
        for row in range(row_length):
            for col in range(col_length):
                if table[row][col]:
                    count = 1
                    for row_above in range(row - 1, -1, -1):
                        if table[row_above][col] >= table[row][col]:
                            count += 1
                        else:
                            break
                    for row_below in range(row + 1, row_length):
                        if table[row_below][col] >= table[row][col]:
                            count += 1
                        else:
                            break
                    result = max(result, table[row][col] * count)
        return result

if __name__ == '__main__':
    pass