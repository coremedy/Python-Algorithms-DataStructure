'''
Created on 2015-11-01
'''

import collections

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms:
            self.height, self.width = len(rooms), len(rooms[0])
            for r in range(self.height):
                for c in range(self.width):
                    if rooms[r][c] == 0:
                        self.bfs(r, c, rooms)
                
    def bfs(self, r, c, rooms):
        # We don't need to record visited nodes here
        # Since visited nodes will have a lower value, which means they will be skipped by comparing values
        dq = collections.deque([(r, c)])
        while dq:
            cell = dq.popleft()
            row, col, val = cell[0], cell[1], rooms[cell[0]][cell[1]]
            if row - 1 >= 0 and rooms[row - 1][col] != -1 and rooms[row - 1][col] > val + 1:
                rooms[row - 1][col] = val + 1
                dq.append((row - 1, col))
            if row + 1 < self.height and rooms[row + 1][col] != -1 and rooms[row + 1][col] > val + 1:
                rooms[row + 1][col] = val + 1
                dq.append((row + 1, col))
            if col - 1 >= 0 and rooms[row][col - 1] != -1 and rooms[row][col - 1] > val + 1:
                rooms[row][col - 1] = val + 1
                dq.append((row, col - 1))
            if col + 1 < self.width and rooms[row][col + 1] != -1 and rooms[row][col + 1] > val + 1:
                rooms[row][col + 1] = val + 1
                dq.append((row, col + 1))

if __name__ == '__main__':
    pass
