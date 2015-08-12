'''
Created on 2015-08-11
'''

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        if matrix is None:
            return result
        row_length = len(matrix)
        if row_length == 0:
            return result
        col_length = len(matrix[0])
        if col_length == 0:
            return result
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        next_movement = 0
        row = 0
        col = 0
        for dummy_index in range(row_length * col_length):
            result.append(matrix[row][col])
            matrix[row][col] = None
            row_next = movement[next_movement][0] + row
            col_next = movement[next_movement][1] + col
            if row_next == row_length or col_next == col_length or matrix[row_next][col_next] is None:
                next_movement = (next_movement + 1) % 4
            row = movement[next_movement][0] + row
            col = movement[next_movement][1] + col
        return result

if __name__ == '__main__':
    pass