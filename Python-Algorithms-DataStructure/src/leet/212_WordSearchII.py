'''
Created on 2015-07-30
'''

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.siblings = dict()
        self.inclusive = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.siblings:
                current.siblings[letter] = TrieNode()
            current = current.siblings[letter]
        current.inclusive = True
        
    def delete(self, word):
        current = self.root
        queue = []
        for letter in word:
            if letter not in current.siblings:
                return
            queue.append((letter, current))
            current = current.siblings[letter]
        if not current.inclusive:
            return
        if len(current.siblings) > 0:
            current.inclusive = False
        else:
            for letter, node in reversed(queue):
                del node.siblings[letter]
                if len(node.siblings) > 0 or node.inclusive:
                    return

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        # Pre-processing
        row_length = len(board)
        if row_length == 0:
            return []
        col_length = len(board[0])
        if col_length == 0:
            return []
        if len(words) == 0:
            return []
        tree = Trie()
        for word in words:
            tree.insert(word)
        recorder = [[False for dummy_col in range(col_length)] for dummy_row in range(row_length)]
        neighbours = zip([1, -1, 0, 0], [0, 0, 1, -1])
        result = set()
        for row in range(row_length):
            for col in range(col_length):
                self.BackTrack(board[row][col], row, col, tree.root, neighbours, row_length, col_length, recorder, board, result, tree)
        return list(result)
        
    def BackTrack(self, prefix, row, col, node, neighbours, row_length, col_length, recorder, board, result, root):
        if board[row][col] not in node.siblings:
            return
        child = node.siblings[board[row][col]]
        recorder[row][col] = True
        for inc_row, inc_col in neighbours:
            row_next, col_next = row + inc_row, col + inc_col
            if row_next >= 0 and row_next < row_length and col_next >= 0 and col_next < col_length and not recorder[row_next][col_next]:
                self.BackTrack(prefix + board[row_next][col_next], row_next, col_next, child, neighbours, row_length, col_length, recorder, board, result, root)
        if child.inclusive is True:
            result.add(prefix)
            root.delete(prefix)
        recorder[row][col] = False

if __name__ == '__main__':
    pass