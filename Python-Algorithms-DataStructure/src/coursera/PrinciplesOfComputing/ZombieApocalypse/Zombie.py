'''
Created on 2015-03-29

https://class.coursera.org/principlescomputing2-002/assignment/view?assignment_id=11
'''

"""
Student portion of Zombie Apocalypse mini-project
"""

import poc_grid # @UnresolvedImport
import poc_queue # @UnresolvedImport
import poc_zombie_gui # @UnresolvedImport

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[ self._grid_width * self._grid_height for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()
        # Initialization
        object_list = self._human_list
        if entity_type == ZOMBIE:
            object_list = self._zombie_list
        for pos in object_list:
            visited.set_full(pos[0], pos[1])
            distance_field[pos[0]][pos[1]] = 0
            boundary.enqueue(pos)
        # Spread the fire ...
        while len(boundary) > 0:
            pos_of_cur_obj = boundary.dequeue()
            four_neighbors = poc_grid.Grid.four_neighbors(self, pos_of_cur_obj[0], pos_of_cur_obj[1])
            for neighbour in four_neighbors:
                if visited.is_empty(neighbour[0], neighbour[1]):
                    if poc_grid.Grid.is_empty(self, neighbour[0], neighbour[1]):
                        visited.set_full(neighbour[0], neighbour[1])
                        if distance_field[pos_of_cur_obj[0]][pos_of_cur_obj[1]] + 1 < distance_field[neighbour[0]][neighbour[1]]:
                            distance_field[neighbour[0]][neighbour[1]] = distance_field[pos_of_cur_obj[0]][pos_of_cur_obj[1]] + 1
                        boundary.enqueue(neighbour)
        return distance_field
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for index in range(0, len(self._human_list)):
            human_pos = self._human_list[index]
            max_distance = zombie_distance[human_pos[0]][human_pos[1]]  
            max_pos = human_pos
            for neighbor in poc_grid.Grid.eight_neighbors(self, human_pos[0], human_pos[1]):
                if poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    if zombie_distance[neighbor[0]][neighbor[1]] > max_distance:
                        max_distance = zombie_distance[neighbor[0]][neighbor[1]]
                        max_pos = neighbor  
            self._human_list[index] = max_pos
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index in range(0, len(self._zombie_list)):
            zombie_pos = self._zombie_list[index]
            min_distance = human_distance[zombie_pos[0]][zombie_pos[1]]  
            min_pos = zombie_pos
            for neighbor in poc_grid.Grid.four_neighbors(self, zombie_pos[0], zombie_pos[1]):
                if poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    if human_distance[neighbor[0]][neighbor[1]] < min_distance:
                        min_distance = human_distance[neighbor[0]][neighbor[1]]
                        min_pos = neighbor
            self._zombie_list[index] = min_pos

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))

if __name__ == '__main__':
    pass