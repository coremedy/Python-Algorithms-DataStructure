'''
Created on 2015-11-04
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) and len(board[0]):
            self.mapping, self.row_len, self.col_len = [0, 1, 1, 0], len(board), len(board[0])
            for row in range(self.row_len):
                for col in range(self.col_len):
                    live = self.calculateLiveNeighbours(row, col, board)
                    if board[row][col]:
                        board[row][col] = 3 if live < 2 or live > 3 else 1
                    else:
                        board[row][col] = 2 if live == 3 else 0
                    if row - 2 >= 0:
                        board[row - 2][col] = self.mapping[board[row - 2][col]]
            for row in range(max(0, self.row_len - 2), self.row_len):
                for col in range(self.col_len):
                    board[row][col] = self.mapping[board[row][col]]

    def calculateLiveNeighbours(self, row, col, board):
        count = 0
        if row - 1 >= 0:
            count = (count + 1) if board[row - 1][col] % 2 else count
            if col - 1 >= 0:
                count = (count + 1) if board[row - 1][col - 1] % 2 else count
            if col + 1 < self.col_len:
                count = (count + 1) if board[row - 1][col + 1] % 2 else count
        if col - 1 >= 0:
            count = (count + 1) if board[row][col - 1] % 2 else count
        if col + 1 < self.col_len:
            count = (count + 1) if board[row][col + 1] % 2 else count
        if row + 1 < self.row_len:
            count = (count + 1) if board[row + 1][col] % 2 else count
            if col - 1 >= 0:
                count = (count + 1) if board[row + 1][col - 1] % 2 else count
            if col + 1 < self.col_len:
                count = (count + 1) if board[row + 1][col + 1] % 2 else count
        return count

if __name__ == '__main__':
    pass