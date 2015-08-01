'''
Created on 2015-08-01
'''

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # Pre - processing
        in_degree_table = [0 for dummy_i in range(numCourses)]
        colour_table = [0 for dummy_i in range(numCourses)]
        adjacency_table = dict()
        for course_pair in prerequisites:
            in_degree_table[course_pair[0]] += 1
            if course_pair[1] not in adjacency_table:
                adjacency_table[course_pair[1]] = set([course_pair[0]])
            else:
                adjacency_table[course_pair[1]].add(course_pair[0])
        # We need to have one or more zero in-degree starting-points
        # If there is none, we have cycles
        if min(in_degree_table) > 0:
            return False
        for course in range(numCourses):
            if in_degree_table[course] == 0:
                has_cycle = [False]
                self.DFS(course, colour_table, adjacency_table, has_cycle)
                if has_cycle[0]:
                    return False
        # If not all nodes are visited, we have cycles
        if min(colour_table) < 2:
            return False
        return True
        
    def DFS(self, course, colour_table, adjacency_table, has_cycle):
        # Black
        if colour_table[course] == 2:
            return
        # Grey
        if colour_table[course] == 1:
            has_cycle[0] = True
            return
        # White
        colour_table[course] = 1
        if course in adjacency_table:
            for neighbour in adjacency_table[course]:
                self.DFS(neighbour, colour_table, adjacency_table, has_cycle)
                if has_cycle[0]:
                    break
            if has_cycle[0]:
                return
        colour_table[course] = 2

if __name__ == '__main__':
    pass