'''
Created on 2015-07-11

Question: Write an algorithm such that if an element in an MxN matrix is 0, 
          its entire row and column are set to 0
'''
import random

def gen_matrix(row_dim, col_dim):
    input_matrix = []
    if row_dim > 0 and col_dim > 0:
        for row in range(0, row_dim):
            input_matrix.append([row + 1 for dummy_col in range(0, col_dim)])
        num_of_zero_cells = random.randint(1, row_dim * col_dim)
        for index in range(0, num_of_zero_cells):
            input_matrix[random.randint(0, row_dim - 1)][random.randint(0, col_dim - 1)] = 0
    print(input_matrix)
    return input_matrix

def set_zeros(input_matrix):
    # Or use array/bitmap
    row_record = set()
    col_record = set()
    for row_index in range(0, len(input_matrix)):
        for col_index in range(0, len(input_matrix[row_index])):
            if input_matrix[row_index][col_index] == 0:
                row_record.add(row_index)
                col_record.add(col_index)
    for row_index in range(0, len(input_matrix)):
        for col_index in range(0, len(input_matrix[row_index])):
            if (row_index in row_record) or (col_index in col_record):
                input_matrix[row_index][col_index] = 0                        
    return input_matrix

if __name__ == '__main__':
    print(set_zeros(gen_matrix(5, 5)))