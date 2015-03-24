'''
Created on 2015-03-24

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=75
'''
import time
import random
import heapq

if __name__ == '__main__':
    start_time = time.time()
    adjacent_matrix = [[0 for dummy_col in range(0, 501)] for dummy_row in range(0, 501)]
    adjacent_list = {}
    number_of_nodes = 0
    number_of_edges = 0
    # Read input - undirected graph
    with open('C:\\testcases\\edges.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 2:
                number_of_nodes = int(data[0])
                number_of_edges = int(data[1])
            else:
                tail = int(data[0])
                head = int(data[1])
                weight = int(data[2])
                adjacent_matrix[tail][head] = adjacent_matrix[head][tail] = weight
                if tail not in adjacent_list:
                    adjacent_list[tail] = set()
                adjacent_list[tail].add(head)
                if head not in adjacent_list:
                    adjacent_list[head] = set()
                adjacent_list[head].add(tail)
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    # Hard-code of maximum value, not good but works out for the input
    vertex_recorder = [10240 for dummy_index in range(0, 501)]
    # Pick up a start vertex randomly
    start_vertex = random.choice(list(adjacent_list.keys()))
    edge_vertex_heap = []
    S = set()
    overall_cost = 0
    while True:
        S.add(start_vertex)
        # We are done
        if len(S) == len(adjacent_list):
            break
        # Put it into heap
        for v in adjacent_list[start_vertex]:
            if v not in S:
                edge_weight = adjacent_matrix[start_vertex][v]
                # Not in heap
                if vertex_recorder[v] == 10240:
                    vertex_recorder[v] = edge_weight
                    heapq.heappush(edge_vertex_heap, (edge_weight, v))
                # In heap already
                else:
                    if vertex_recorder[v] != edge_weight:
                        # Modify the recorder when best value appears
                        if edge_weight < vertex_recorder[v]:
                            vertex_recorder[v] = edge_weight
                            heapq.heappush(edge_vertex_heap, (edge_weight, v))
        # Seek for next start node
        while True:
            tup = heapq.heappop(edge_vertex_heap)
            # Take care of redundancy
            if tup[1] not in S:
                if vertex_recorder[tup[1]] == tup[0]:
                    start_vertex = tup[1]
                    overall_cost += tup[0]
                    break
        # Done
    print('Prim\'s procedure --- %s seconds ---' % (time.time() - start_time))
    print(overall_cost)