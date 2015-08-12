'''
Created on 2015-08-12
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row_length = len(matrix)
        if row_length == 0:
            return
        col_length = len(matrix[0])
        if row_length == 0:
            return
        # Check first row and first col
        set_first_row_to_zero = False
        for index in range(col_length):
            if matrix[0][index] == 0:
                set_first_row_to_zero = True
                break
        set_first_col_to_zero = False
        for index in range(row_length):
            if matrix[index][0] == 0:
                set_first_col_to_zero = True
                break
        # Use first row and first col as recorder
        for row_index in range(1, row_length):
            for col_index in range(1, col_length):
                if matrix[row_index][col_index] == 0:
                    matrix[row_index][0] = 0
                    matrix[0][col_index] = 0
        # Update
        for row_index in range(1, row_length):
            if matrix[row_index][0] == 0:
                for col_index in range(1, col_length):
                    matrix[row_index][col_index] = 0
        for col_index in range(1, col_length):
            if matrix[0][col_index] == 0:
                for row_index in range(1, row_length):
                    matrix[row_index][col_index] = 0
        # Finally, update first row and first col
        if set_first_row_to_zero:
            for index in range(col_length):
                matrix[0][index] = 0
        if set_first_col_to_zero:
            for index in range(row_length):
                matrix[index][0] = 0

if __name__ == '__main__':
    pass