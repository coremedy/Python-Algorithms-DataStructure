'''
Created on 2015-08-17
'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row_length = len(matrix)
        if row_length == 0:
            return False
        col_length = len(matrix[0])
        if col_length == 0:
            return False
        begin = 0
        end = row_length * col_length - 1
        while begin != end:
            mid = (begin + end) // 2
            if matrix[mid // col_length][mid % col_length] == target:
                return True
            elif matrix[mid // col_length][mid % col_length] > target:
                end = mid
            else:
                begin = mid + 1
        if matrix[begin // col_length][begin % col_length] == target:
            return True
        return False

if __name__ == '__main__':
    pass