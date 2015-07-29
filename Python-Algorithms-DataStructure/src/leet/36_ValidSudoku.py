'''
Created on 2015-07-29
'''

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # Check row
        row_table = [dict() for dummy_index in range(9)]
        col_table = [dict() for dummy_index in range(9)]
        sqr_table = [dict() for dummy_index in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    value = int(board[row][col])
                    # Rule 1
                    if value < 1 or value > 9:
                        return False
                    # Rule 2
                    if value not in row_table[row]:
                        row_table[row][value] = True
                    else:
                        return False
                    # Rule 3
                    if value not in col_table[col]:
                        col_table[col][value] = True
                    else:
                        return False
                    # Rule 4
                    sqr_index = (col // 3) + 3 * (row // 3)
                    if value not in sqr_table[sqr_index]:
                        sqr_table[sqr_index][value] = True
                    else:
                        return False
        return True

if __name__ == '__main__':
    pass