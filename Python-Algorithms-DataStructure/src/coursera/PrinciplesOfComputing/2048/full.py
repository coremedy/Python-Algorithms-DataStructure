'''
Created on 2015-02-24

https://class.coursera.org/principlescomputing1-002/wiki/view?page=2048
'''

"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    if line is None:
        return []
    if len(line) < 2:
        return line
    # valid input
    result_list = [0 for dummy_index in range(0, len(line))]
    merged = False
    last_elem_index = -1
    for index in range(0, len(line)):
        # bypass zero
        if line[index] == 0:
            continue
        else:
            # valid merge situation
            if (result_list[last_elem_index] == line[index]) and (merged == False):
                result_list[last_elem_index] += line[index]
                merged = True
            else:
                last_elem_index += 1
                result_list[last_elem_index] = line[index]
                if merged == True:
                    merged = False
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid_tile = [[0 for dummy_col in range(0, grid_width)] for dummy_row in range(0, grid_height)]
        self._grid_headers = [[] for dummy_row in range(0, RIGHT + 1)]
        for row in range(0, grid_height):
            self._grid_headers[LEFT].append((row, 0))
            self._grid_headers[RIGHT].append((row, grid_width - 1))
        for col in range(0, grid_width):
            self._grid_headers[UP].append((0, col))
            self._grid_headers[DOWN].append((grid_height - 1, col))
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        for row in range(0, self._grid_height):
            for col in range(0, self._grid_width):
                self._grid_tile[row][col] = 0
        # at this step, all cells should be available
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        result = ''
        for row in range(0, self._grid_height):
            result += str(self._grid_tile[row]) + '\n'
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        row_increment = OFFSETS[direction][0]
        col_increment = OFFSETS[direction][1]
        changed = False
        for header in self._grid_headers[direction]:
            row_header = header[0]
            col_header = header[1]
            source_line = []
            # get the source line first
            while (row_header >= 0) and (col_header >= 0) and (row_header < self._grid_height) and (col_header < self._grid_width):
                source_line.append(self.get_tile(row_header, col_header))
                row_header += row_increment
                col_header += col_increment
            # merge
            result_line = merge(source_line)
            # write the result back
            row_header = header[0]
            col_header = header[1]
            result_line_index = 0
            while (row_header >= 0) and (col_header >= 0) and (row_header < self._grid_height) and (col_header < self._grid_width):
                self.set_tile(row_header, col_header, result_line[result_line_index])
                if result_line[result_line_index] != source_line[result_line_index]:
                    changed = True
                result_line_index += 1
                row_header += row_increment
                col_header += col_increment
        if changed:
            self.new_tile()       

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        # complete search ....
        non_zero_count = 0;
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid_tile[row][col] == 0:
                    non_zero_count += 1
        random_choice = random.randrange(0, non_zero_count)
        count = 0
        # another search ....
        generated_new_tile = False
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if generated_new_tile == False and self._grid_tile[row][col] == 0:
                    if count != random_choice:
                        count += 1   
                    else:
                        if random.randrange(0,100) < 10:
                            self.set_tile(row, col ,4)
                        else:
                            self.set_tile(row, col ,2)
                        generated_new_tile = True

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid_tile[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid_tile[row][col]

if __name__ == '__main__':
    # poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
    pass