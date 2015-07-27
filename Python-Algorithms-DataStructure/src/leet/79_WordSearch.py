'''
Created on 2015-07-27
'''
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        board_height = len(board)
        if board_height == 0:
            return False
        board_width = len(board[0])
        if board_width == 0:
            return False
        if len(word) == 0:
            return False
        start_dict = dict()
        movement_dict = dict()
        for row in range(board_height):
            for col in range(board_width):
                if board[row][col] not in start_dict:
                    start_dict[board[row][col]] = [(row, col)]
                else:
                    start_dict[board[row][col]].append((row, col))
                movement_dict[(row, col)] = []
                if col > 0:
                    movement_dict[(row, col)].append((row, col - 1))
                if col < board_width - 1:
                    movement_dict[(row, col)].append((row, col + 1))
                if row > 0:
                    movement_dict[(row, col)].append((row - 1, col))
                if row < board_height - 1:
                    movement_dict[(row, col)].append((row + 1, col))
        if word[0] in start_dict:
            for current in start_dict[word[0]]:
                result = [False]
                self.BackTrack(current, board, 0, word, movement_dict, result, set([current]))
                if result[0]:
                    return True
        return False
        
    def BackTrack(self, current_cell, board, current_index, word, movement_dict, result, cache_set):
        if current_index == len(word) - 1:
            result[0] = True
            return
        for next_cell in movement_dict[current_cell]:
            if next_cell not in cache_set and board[next_cell[0]][next_cell[1]] == word[current_index + 1]:
                self.BackTrack(next_cell, board, current_index + 1, word, movement_dict, result, cache_set | set([next_cell]))
                if result[0]:
                    break

if __name__ == '__main__':
    pass