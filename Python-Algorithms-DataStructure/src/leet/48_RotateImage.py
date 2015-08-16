'''
Created on 2015-08-16
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, input_matrix):
        if len(input_matrix) == 0 or len(input_matrix) == 1:
            return
        dim_minus_one = len(input_matrix) - 1
        for row_index in range(0, len(input_matrix) // 2):
            for col_index in range(row_index, dim_minus_one - row_index):
                temp_val = input_matrix[row_index][col_index]
                input_matrix[row_index][col_index] = input_matrix[dim_minus_one - col_index][row_index]
                input_matrix[dim_minus_one - col_index][row_index] = input_matrix[dim_minus_one - row_index][dim_minus_one - col_index]
                input_matrix[dim_minus_one - row_index][dim_minus_one - col_index] = input_matrix[col_index][dim_minus_one - row_index]
                input_matrix[col_index][dim_minus_one - row_index] = temp_val
        return

if __name__ == '__main__':
    pass