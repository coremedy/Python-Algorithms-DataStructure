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

def dijkstra(source):
    dijkstra_distance = [4294967296 for dummy_index in range(0, number_of_vertices + 1)]
    dijkstra_flag = [True for dummy_index in range(0, number_of_vertices + 1)]
    dijkstra_distance[source] = 0
    
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
    return dijkstra_distance

def bellman_ford():
    # Using map function will result in more time ...
    bellman_ford_dist = [4294967296 for dummy_index in range(0, number_of_vertices + 1)]
    bellman_ford_dist[0] = 0
    
    for iter_index in range(1, number_of_vertices + 1):
        for head_vertex in in_dict_with_extra_source.keys():
            for tail_vertex in in_dict_with_extra_source[head_vertex]:
                if bellman_ford_dist[tail_vertex] + adjacent_matrix[tail_vertex][head_vertex] < bellman_ford_dist[head_vertex]:
                    if iter_index == number_of_vertices:
                        return None
                    else:
                        bellman_ford_dist[head_vertex] = bellman_ford_dist[tail_vertex] + adjacent_matrix[tail_vertex][head_vertex]    
    return bellman_ford_dist

if __name__ == '__main__':
    start_time = time.time()
    # For Dijkstra
    weight_dict = dict()
    out_dict_original = dict()
    # For Bellman-Ford
    in_dict_with_extra_source = dict()
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
                adjacent_matrix = [[0 for dummy_col in range(0, number_of_vertices + 1)] for dummy_row in range(0, number_of_vertices + 1)]
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
                if head not in in_dict_with_extra_source:
                    in_dict_with_extra_source[head] = set()
                    in_dict_with_extra_source[head].add(0)
                    in_dict_with_extra_source[head].add(tail)
                else:
                    in_dict_with_extra_source[head].add(tail)   
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    bellman_ford_result = bellman_ford()
    if bellman_ford_result is not None:
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        start_time = time.time()
        # Adjust the matrix
        for tup in weight_dict.keys():
            adjacent_matrix[tup[0]][tup[1]] = weight_dict[tup] + bellman_ford_result[tup[0]] - bellman_ford_result[tup[1]]
        # N Dijkstra
        min_distance = 4294967296
        for source in range(1, number_of_vertices + 1):
            dijkstra_result = dijkstra(source)
            for target in range(1, number_of_vertices + 1):
                if target != source:
                    min_distance = min(min_distance, dijkstra_result[target] - bellman_ford_result[source] + bellman_ford_result[target])
            heap_element_finder.clear()
        print('n Dijkstra --- %s seconds ---' % (time.time() - start_time))
        print(min_distance)
    else:
        print('Bellman-ford --- %s seconds ---' % (time.time() - start_time))
        print('There is a negative cycle for this graph')