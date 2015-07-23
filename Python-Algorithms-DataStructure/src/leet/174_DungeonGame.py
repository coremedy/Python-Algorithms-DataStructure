'''
Created on 2015-07-22
'''

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        row_length = len(dungeon)
        col_length = len(dungeon[0])
        # The minimal HP to enter one cell and move to the end without dying
        table = [[0 for dummy_col in range(col_length)] for dummy_row in range(row_length)]
        table[row_length - 1][col_length - 1] = max(0, -dungeon[row_length - 1][col_length - 1]) + 1
        for row in range(row_length - 1, -1, -1):
            for col in range(col_length - 1, -1, -1):
                if not ((row == row_length - 1) and (col == col_length - 1)):
                    min_from_previous = None
                    if row == row_length - 1:
                        min_from_previous = table[row][col + 1]
                    elif col == col_length - 1:
                        min_from_previous = table[row + 1][col]
                    else:
                        min_from_previous = min(table[row][col + 1], table[row + 1][col])
                    # Safe
                    if dungeon[row][col] == 0:
                        table[row][col] = min_from_previous
                    # Need more HP
                    elif dungeon[row][col] < 0:
                        table[row][col] = min_from_previous - dungeon[row][col]
                    # Need less HP, but at least 1
                    else:
                        val = min_from_previous - dungeon[row][col]
                        if val <= 0:
                            val = 1
                        table[row][col] = val
        return table[0][0]

if __name__ == '__main__':
    pass