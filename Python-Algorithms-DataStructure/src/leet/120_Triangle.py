'''
Created on 2015-07-18
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        row_length = len(triangle)
        if row_length == 0:
            return 0
        table = [0 for dummy_col in range(len(triangle[row_length - 1]))]
        for row in range(row_length):
            if row == 0:
                for col in range(len(triangle[row])):
                    table[col] = triangle[row][col]
            else:
                for col in range(len(triangle[row]) - 1, -1, -1):
                    if col == len(triangle[row]) - 1:
                        table[col] = table[col - 1] + triangle[row][col]
                    elif col == 0:
                        table[col] = table[col] + triangle[row][col]
                    else:
                        table[col] = min(table[col] + triangle[row][col], table[col - 1] + triangle[row][col])
        return min(table)

if __name__ == '__main__':
    pass