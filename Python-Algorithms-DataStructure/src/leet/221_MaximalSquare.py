'''
Created on 2015-07-18
'''


# Use int() to convert str to int
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        result = 0
        row_length = len(matrix)
        if row_length == 0:
            return result * result
        if not isinstance(matrix[0], list):
            # An 'simple' array ...
            for index in range(0, row_length):
                result = max(int(matrix[index]), result)
            return result * result
        else:
            col_length = len(matrix[0])
            if col_length == 0:
                return result
            for index in range(0, col_length):
                matrix[0][index] = int(matrix[0][index])
                result = max(matrix[0][index], result)
            for index in range(0, row_length):
                matrix[index][0] = int(matrix[index][0])
                result = max(matrix[index][0], result)           
            # All right ...
            for row in range(1, row_length):
                for col in range(1, col_length):
                    if int(matrix[row][col]):
                        matrix[row][col] = min(matrix[row][col - 1], matrix[row - 1][col], matrix[row - 1][col - 1]) + 1
                        result = max(result, matrix[row][col])
                    else:
                        matrix[row][col] = 0
            return result * result

if __name__ == '__main__':
    pass