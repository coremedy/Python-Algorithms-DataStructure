'''
Created on 2015-02-19

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=96
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

def dijkstra():
    while True:
        current_vertex_dist_list = heap_pop_min()
        if current_vertex_dist_list is None:
            # We are done
            break
        # Confirm tail vertex with least distance value
        current_tail = current_vertex_dist_list[1]
        current_tail_dist = current_vertex_dist_list[0]
        # Mark the tail vertex as visited
        vertex_status_list[current_tail] = False
        # Search for head vertex
        for current_head_tuple in adjacency_list[current_tail]:
            current_head = current_head_tuple[0]
            current_head_dist = current_head_tuple[1]
            # Unvisited head vertex (valid)
            if vertex_status_list[current_head]:
                # The distance of head vertex can be released
                if current_tail_dist + current_head_dist < vertex_dist_result_list[current_head]:
                    heap_delete(current_head)
                    heap_push(current_head, current_tail_dist + current_head_dist)
                    # Release
                    vertex_dist_result_list[current_head] = current_tail_dist + current_head_dist

if __name__ == '__main__':
    start_time = time.time()
    # Graph data structure
    adjacency_list = [[] for dummy_i in range(0, 201)]
    # Read input
    with open('C:\\testcases\\dijkstraData.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            edge = line.strip().split()
            tail = int(edge[0])
            for i in range(1, len(edge)):
                comma_pos = edge[i].find(',')
                head = int(edge[i][:comma_pos])
                weight = int(edge[i][comma_pos + 1:])
                adjacency_list[tail].append((head, weight))
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    # Heap data structure
    vertex_dist_heap = []
    heap_element_finder = dict()
    # Other data structure: distance of all target vertices, 1000000 is the max value
    vertex_dist_result_list = [1000000 for dummy_i in range(0, 201)]
    # Other data structure: keep track of vertex status
    vertex_status_list = [True for dummy_i in range(0, 201)]
    vertex_dist_result_list[1] = 0
    # Push the source vertex to heap
    heap_push(1, 0)
    # Start Dijkstra procedure
    dijkstra()
    # End Dijkstra procedure
    print('Processing graph --- %s seconds ---' % (time.time() - start_time))
    final_result_list = []
    for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        final_result_list.append(vertex_dist_result_list[i])
    print(final_result_list)