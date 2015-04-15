'''
Created on 2015-04-15

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=89
'''

import time
import heapq
import copy

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

def dijkstra(source):
    heap_push(source, dijkstra_distance[source])
    while True:
        current_vertex_dist_list = heap_pop_min()
        if current_vertex_dist_list is None:
            break
        current_tail = current_vertex_dist_list[1]
        dijkstra_flag[current_tail] = False
        if current_tail in out_dict_original:
            for current_head in out_dict_original[current_tail]:
                if dijkstra_flag[current_head]:
                    if current_vertex_dist_list[0] + adjacent_matrix[current_tail][current_head] < dijkstra_distance[current_head]:
                        heap_delete(current_head)
                        dijkstra_distance[current_head] = current_vertex_dist_list[0] + adjacent_matrix[current_tail][current_head]
                        heap_push(current_head, dijkstra_distance[current_head])

def bellman_ford():
    bellman_ford_dist_prev = [4294967296 for dummy_index in range_zero_to_limit]
    bellman_ford_dist_prev[0] = 0
    bellman_ford_dist_next = copy.deepcopy(bellman_ford_dist_prev)
    for index in range_one_to_limit:
        for edge in all_edges_plus_dummy_edges:
            if bellman_ford_dist_prev[edge[0]] + adjacent_matrix[edge[0]][edge[1]] < bellman_ford_dist_prev[edge[1]]:
                bellman_ford_dist_next[edge[1]] = bellman_ford_dist_prev[edge[0]] + adjacent_matrix[edge[0]][edge[1]]
        if index < number_of_vertices:
            bellman_ford_dist_prev = copy.deepcopy(bellman_ford_dist_next)
    # Detect negative cycle
    for index in range_one_to_limit:
        if bellman_ford_dist_next[index] != bellman_ford_dist_prev[index]:
            return None
    return bellman_ford_dist_next

if __name__ == '__main__':
    start_time = time.time()
    # For Dijkstra
    weight_dict = dict()
    out_dict_original = dict()
    # Heap data structure
    vertex_dist_heap = []
    heap_element_finder = dict()
    # Read input from file
    with open('C:\\testcases\\g3.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 2:
                number_of_vertices = int(data[0])
                number_of_edge = int(data[1])
                range_zero_to_limit = [x for x in range(0, number_of_vertices + 1)]
                range_one_to_limit = [x for x in range(1, number_of_vertices + 1)]
                adjacent_matrix = [[0 for dummy_col in range_zero_to_limit] for dummy_row in range_zero_to_limit]
                # For Bellman-Ford
                all_edges_plus_dummy_edges = [(0, x) for x in range_one_to_limit]
                # For Dijkstra     
                dijkstra_distance = [4294967296 for dummy_index in range_zero_to_limit]
                dijkstra_flag = [True for dummy_index in range_zero_to_limit]
            else:
                tail = int(data[0])
                head = int(data[1])
                weight = int(data[2])
                adjacent_matrix[tail][head] = weight
                all_edges_plus_dummy_edges.append((tail, head))
                weight_dict[(tail, head)] = weight
                if tail in out_dict_original:
                    out_dict_original[tail].add(head)
                else:
                    out_dict_original[tail] = set()
                    out_dict_original[tail].add(head)
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    bellman_ford_dist = bellman_ford()
    if bellman_ford_dist is not None:
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        start_time = time.time()
        # Adjust the matrix
        for tup in weight_dict.keys():
            adjacent_matrix[tup[0]][tup[1]] = weight_dict[tup] + bellman_ford_dist[tup[0]] - bellman_ford_dist[tup[1]]
        # N Dijkstra
        min_distance = 4294967296
        for source in range_one_to_limit:
            dijkstra_distance[source] = 0
            dijkstra(source)
            for target in range_one_to_limit:
                if target != source:
                    min_distance = min(min_distance, dijkstra_distance[target] - bellman_ford_dist[source] + bellman_ford_dist[target])
                dijkstra_distance[target] = 4294967296
                dijkstra_flag[target] = True
            heap_element_finder.clear()
        print('n Dijkstra --- %s seconds ---' % (time.time() - start_time))
        print(min_distance)
    else:
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        print('There is a negative cycle for this graph')