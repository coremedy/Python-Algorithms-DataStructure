'''
Created on 2015-07-11

Question: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
          write a method to rotate the image by 90 degrees
          Can you do this in place?
'''

def gen_square_matrix(dim):
    input_matrix = []
    for row in range(0, dim):
        input_matrix.append([row + 1 for dummy_col in range(0, dim)])
    return input_matrix

def rotate_matrix_clockwise(input_matrix):
    if len(input_matrix) == 0 or len(input_matrix) == 1:
        return input_matrix
    dim_minus_one = len(input_matrix) - 1
    for row_index in range(0, len(input_matrix) // 2):
        for col_index in range(row_index, dim_minus_one - row_index):
            temp_val = input_matrix[row_index][col_index]
            input_matrix[row_index][col_index] = input_matrix[dim_minus_one - col_index][row_index]
            input_matrix[dim_minus_one - col_index][row_index] = input_matrix[dim_minus_one - row_index][dim_minus_one - col_index]
            input_matrix[dim_minus_one - row_index][dim_minus_one - col_index] = input_matrix[col_index][dim_minus_one - row_index]
            input_matrix[col_index][dim_minus_one - row_index] = temp_val
    return input_matrix

if __name__ == '__main__':
    print(rotate_matrix_clockwise(gen_square_matrix(7)))