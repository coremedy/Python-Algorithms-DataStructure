'''
Created on 2015-07-29
'''

class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        result = []
        self.BackTrack(0, n, [-1 for dummy_index in range(n)], result)
        if len(result) == 0:
            return []
        solutions = []
        for candidate in result:
            chess_board = [['.' for dumm_col in range(n)] for dummy_row in range(n)]
            for index in range(n):
                chess_board[candidate[index]][index] = 'Q'
            one_solution = []
            for index in range(n):
                one_solution.append(''.join(chess_board[index]))
            solutions.append(one_solution)
        return solutions

    def BackTrack(self, current_col, n, table, result):
        if current_col == n:
            result.append(tuple(table))
            return
        for current_row in range(n):
            if not self.Collide(current_col, current_row, table):
                table[current_col] = current_row
                self.BackTrack(current_col + 1, n, table, result)
    
    def Collide(self, current_col, current_row, table):
        if current_col == 0:
            return False
        for index in range(0, current_col):
            if current_row == table[index]:
                return True
            y = current_row - table[index]
            x = current_col - index
            if x == y or x == -y:
                return True
        return False

if __name__ == '__main__':
    pass