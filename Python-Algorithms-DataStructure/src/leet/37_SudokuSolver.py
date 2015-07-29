'''
Created on 2015-07-29
'''

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        # Pre-processing ...
        row_table = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for dummy_index in range(9)]
        col_table = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for dummy_index in range(9)]
        sqr_table = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for dummy_index in range(9)]
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    value = int(board[row][col])
                    row_table[row].remove(value)
                    col_table[col].remove(value)
                    sqr_table[(col // 3) + 3 * (row // 3)].remove(value)
                else:
                    empty_cells.append((row, col))
        # Backtrack on empty_cells
        stop_sign = [False]
        self.BackTrack(empty_cells, row_table, col_table, sqr_table, board, stop_sign)
        
    def BackTrack(self, empty_cells, row_table, col_table, sqr_table, board, stop_sign):
        if len(empty_cells) == 0:
            stop_sign[0] = True
            return
        current_cell = empty_cells[0]
        intersection_set = row_table[current_cell[0]] & col_table[current_cell[1]]
        intersection_set = intersection_set & sqr_table[(current_cell[1] // 3) + 3 * (current_cell[0] // 3)]
        if len(intersection_set) == 0:
            return
        for candidate in intersection_set:
            row_table[current_cell[0]].remove(candidate)
            col_table[current_cell[1]].remove(candidate)
            sqr_table[(current_cell[1] // 3) + 3 * (current_cell[0] // 3)].remove(candidate)
            board[current_cell[0]][current_cell[1]] = str(candidate)
            self.BackTrack(empty_cells[1:], row_table, col_table, sqr_table, board, stop_sign)
            if stop_sign[0]:
                break
            sqr_table[(current_cell[1] // 3) + 3 * (current_cell[0] // 3)].add(candidate)
            col_table[current_cell[1]].add(candidate)
            row_table[current_cell[0]].add(candidate)

if __name__ == '__main__':
    pass