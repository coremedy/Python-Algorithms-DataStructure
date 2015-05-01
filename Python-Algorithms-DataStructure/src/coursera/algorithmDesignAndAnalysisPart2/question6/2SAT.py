'''
Created on 2015-04-30

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=97
'''

import time

def dfs_iterative_phase_one(vertex):
    reversed_graph[vertex][0] = True
    while True:
        move_to_next = False
        if len(reversed_graph[vertex]) > 1:
            for neighbour in reversed_graph[vertex][1:]:
                if reversed_graph[neighbour][0] is False:
                    runtime_stack.append(vertex)
                    vertex = neighbour
                    reversed_graph[neighbour][0] = True
                    move_to_next = True
                    break
        if move_to_next:
            continue
        else:
            topological_order_stack.append(vertex)
            if len(runtime_stack) > 0:
                vertex = runtime_stack.pop()
                continue
            else:
                break

def dfs_iterative_phase_two(vertex):
    normal_graph[vertex][0] = True
    record = set()
    while True:
        move_to_next = False
        if len(normal_graph[vertex]) > 1:
            for neighbour in normal_graph[vertex][1:]:
                if normal_graph[neighbour][0] is False:
                    runtime_stack.append(vertex)
                    vertex = neighbour
                    normal_graph[neighbour][0] = True
                    move_to_next = True
                    break
        if move_to_next:
            continue
        else:
            record.add(vertex)
            if len(runtime_stack) > 0:
                vertex = runtime_stack.pop()
                continue
            else:
                break
    return record

def add_edge(graph, edge):
    if edge[0] not in graph:
        graph[edge[0]] = [False, edge[1]]
    else:
        graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
        graph[edge[1]] = [False] 

if __name__ == '__main__':
    start_time = time.time()
    normal_graph = dict()
    reversed_graph = dict()
    with open('C:\\testcases\\2sat6.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 1:
                number_of_rules = int(data[0])
            else:
                edge1 = (-int(data[0]), int(data[1]))
                add_edge(normal_graph, edge1)
                add_edge(reversed_graph, edge1[::-1])
                edge2 = (-int(data[1]), int(data[0]))
                add_edge(normal_graph, edge2)
                add_edge(reversed_graph, edge2[::-1])
    print('Processing input and creating data structure: --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    topological_order_stack = []
    runtime_stack = []
    for key in reversed_graph.keys():
        if reversed_graph[key][0] is False:
            dfs_iterative_phase_one(key)
    not_match = False
    while len(topological_order_stack) > 0:
        index = topological_order_stack.pop()
        if normal_graph[index][0] is False:
            result = dfs_iterative_phase_two(index)
            if len(result) > 1:
                for element in result:
                    if -element in result:
                        not_match = True
                        break
    print(not_match)                       
    print('Kosaraju: --- %s seconds ---' % (time.time() - start_time))