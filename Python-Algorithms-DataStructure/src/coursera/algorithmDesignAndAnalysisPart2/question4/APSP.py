'''
Created on 2015-04-15

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=89
'''

import time
import heapq

def heap_push(vertex, dist):
    vertex_dist_list = [dist, vertex]
    heap_element_finder[vertex] = vertex_dist_list
    heapq.heappush(vertex_dist_heap, vertex_dist_list)

def heap_delete(vertex):
    if vertex in heap_element_finder:
        vertex_dist_list = heap_element_finder[vertex]
        # Do not touch the distance or you will violate the heap property
        # Just need to mark vertex as invalid
        vertex_dist_list[1] = -1

def heap_pop_min():
    valid_vertex_dist_list = None
    while len(vertex_dist_heap) > 0:
        vertex_dist_list = heapq.heappop(vertex_dist_heap)
        if vertex_dist_list[1] == -1:
            continue
        else:
            valid_vertex_dist_list = vertex_dist_list
            break
    return valid_vertex_dist_list

def bellman_ford():
    for index in range(1, number_of_vertices + 1):
        for head in range(1, number_of_vertices + 1):
            if head in in_dict_johnson:
                for tail in in_dict_johnson[head]:
                    if bellman_ford_dist_prev[tail] + adjacent_matrix[tail][head] < bellman_ford_dist_prev[head]:
                        bellman_ford_dist_next[head] = bellman_ford_dist_prev[tail] + adjacent_matrix[tail][head]
        if index < number_of_vertices:
            for head in range(0, number_of_vertices + 1):
                bellman_ford_dist_prev[head] = bellman_ford_dist_next[head]
    # Detect negative cycle
    for index in range(0, len(bellman_ford_dist_prev)):
        if bellman_ford_dist_next[index] != bellman_ford_dist_prev[index]:
            return False
    return True

if __name__ == '__main__':
    start_time = time.time()
    # For Dijkstra
    weight_dict = dict()
    out_dict_original = dict()
    # For Bellman-Ford
    in_dict_johnson = dict()
    # Read input from file
    with open('C:\\testcases\\g3.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 2:
                number_of_vertices = int(data[0])
                number_of_edge = int(data[1])
                adjacent_matrix = [[0 for dummy_col in range(0, number_of_vertices + 1)] for dummy_row in range(0, number_of_vertices + 1)]
                # Insert some data first
                for vertex in range(1, number_of_vertices + 1):
                    in_dict_johnson[vertex] = set()
                    in_dict_johnson[vertex].add(0)
            else:
                tail = int(data[0])
                head = int(data[1])
                weight = int(data[2])
                adjacent_matrix[tail][head] = weight
                weight_dict[(tail, head)] = weight
                if tail in out_dict_original:
                    out_dict_original[tail].add(head)
                else:
                    out_dict_original[tail] = set()
                    out_dict_original[tail].add(head)
                
                in_dict_johnson[head].add(tail)
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    bellman_ford_dist_prev = [4294967296 for vertex in range(0, 1001)]
    bellman_ford_dist_prev[0] = 0
    bellman_ford_dist_next = [4294967296 for vertex in range(0, 1001)]
    bellman_ford_dist_next[0] = 0
    if bellman_ford():
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        start_time = time.time()
        # Adjust the matrix
        for tup in weight_dict.keys():
            adjacent_matrix[tup[0]][tup[1]] = weight_dict[tup] + bellman_ford_dist_next[tup[0]] - bellman_ford_dist_next[tup[1]]
        # Heap data structure
        vertex_dist_heap = []
        heap_element_finder = dict()
        # TODO
        print('n Dijkstra --- %s seconds ---' % (time.time() - start_time))
    else:
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        print('There is a negative cycle for this graph')