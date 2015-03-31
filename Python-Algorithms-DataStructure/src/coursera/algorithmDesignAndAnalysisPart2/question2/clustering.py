'''
Created on 2015-03-31

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=79
'''

import time
import heapq

class union_find(object):
    
    def __init__(self, size):
        # Neglect 0 here
        self._pset = [index for index in range(0, size + 1)]
        self._components = size
    
    def findSet(self, vertex):
        if vertex == self._pset[vertex]:
            return vertex
        else:
            # Flatten the tree
            self._pset[vertex] = self.findSet(self._pset[vertex])
            return self._pset[vertex]
    
    def isSameSet(self, vertex_a, vertex_b):
        return self.findSet(vertex_a) == self.findSet(vertex_b)
    
    def unionSet(self, vertex_a, vertex_b):
        root_a = self.findSet(vertex_a)
        root_b = self.findSet(vertex_b)
        if root_a != root_b:
            self._pset[root_a] = root_b
            self._components -= 1
    
    def components(self):
        return self._components

if __name__ == '__main__':
    start_time = time.time()
    edge_heap = []
    number_of_vertices = 0
    # Read input
    with open('C:\\testcases\\clustering1.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 1:
                number_of_vertices = int(data[0])
            else:
                heapq.heappush(edge_heap, (int(data[2]), int(data[0]), int(data[1])))
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    uf = union_find(number_of_vertices)
    while uf.components() > 4:
        tup = heapq.heappop(edge_heap)
        if not uf.isSameSet(tup[1], tup[2]):
            uf.unionSet(tup[1], tup[2])
    # Get rid of edges already in connected components
    while True:
        tup = heapq.heappop(edge_heap)
        if not uf.isSameSet(tup[1], tup[2]):
            print(tup[0])
            break
    print('Clustering --- %s seconds ---' % (time.time() - start_time))