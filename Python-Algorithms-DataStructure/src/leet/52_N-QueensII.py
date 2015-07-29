'''
Created on 2015-07-29
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        counter = [0]
        self.BackTrack(0, n, [-1 for dummy_index in range(n)], counter)
        return counter[0]
    
    def BackTrack(self, current_col, n, table, counter):
        if current_col == n:
            counter[0] += 1
            return
        for current_row in range(n):
            if not self.Collide(current_col, current_row, table):
                table[current_col] = current_row
                self.BackTrack(current_col + 1, n, table, counter)
    
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