'''
Created on 2015-08-01
'''

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        # Pre-processing
        row_length = len(board)
        if row_length == 0:
            return
        col_length = len(board[0])
        if col_length == 0:
            return
        can_flip = [[True for col in range(col_length)] for row in range(row_length)]
        for row in range(row_length):
            if row == 0 or row == row_length - 1:
                for col in range(col_length):
                    if can_flip[row][col] and board[row][col] == 'O':
                        self.BFS(row, col, can_flip, row_length, col_length, board)
            else:
                if can_flip[row][0] and board[row][0] == 'O':
                    self.BFS(row, 0, can_flip, row_length, col_length, board)
                if can_flip[row][col_length - 1] and board[row][col_length - 1] == 'O':
                    self.BFS(row, col_length - 1, can_flip, row_length, col_length, board)
        for row in range(row_length):
            for col in range(col_length):
                if can_flip[row][col]:
                    board[row][col] = 'X'
    
    def BFS(self, row, col, can_flip, row_length, col_length, board):
        nodes = [(row, col)]
        nodes_start = 0
        nodes_end = 1
        while True:
            count = 0
            for index in range(nodes_start, nodes_end):
                if can_flip[nodes[index][0]][nodes[index][1]] and board[nodes[index][0]][nodes[index][1]] == 'O':
                    for (row_inc, col_inc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        row_new = nodes[index][0] + row_inc
                        col_new = nodes[index][1] + col_inc                    
                        if row_new >= 0 and row_new < row_length and col_new >= 0 and col_new < col_length and can_flip[row_new][col_new] and board[row_new][col_new] == 'O':
                            nodes.append((row_new, col_new))
                            count += 1
                    can_flip[nodes[index][0]][nodes[index][1]] = False
            if count == 0:
                break
            nodes_start, nodes_end = nodes_end, nodes_end + count

if __name__ == '__main__':
    pass