'''
Created on 2015-08-12
'''

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        result = [[None for dummy_col in range(n)] for dummy_row in range(n)]
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        next_movement = 0
        row = 0
        col = 0
        for e in range(1, n * n + 1):
            result[row][col] = e
            row_next = movement[next_movement][0] + row
            col_next = movement[next_movement][1] + col            
            if row_next == n or col_next == n or result[row_next][col_next] is not None:
                next_movement = (next_movement + 1) % 4
            row = movement[next_movement][0] + row
            col = movement[next_movement][1] + col           
        return result

if __name__ == '__main__':
    pass