'''
Created on 2015-10-20
Divide and Conquer: T(n) = 3T(n/2) + constant
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, c = len(matrix), len(matrix[0]) - 1 
        for r in range(m):
            while c >= 0 and matrix[r][c] > target:
                c -= 1
            if matrix[r][c] == target:
                return True
        return False

if __name__ == '__main__':
    pass