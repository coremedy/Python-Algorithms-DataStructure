'''
Created on 2015-02-10

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=57
'''

import time
import heapq

# Seems someone meets with the issue of "Python maximum recursion depth exceeded"
# A iterative version can solve this issue
def dfs_iterative(v, phase):
    size_of_scc = 0
    graph = None
    if phase == 1:
        graph = graph_phase_one
    else:
        graph = graph_phase_two
    graph[v][0] = True
    while True:
        found = False
        if len(graph[v]) > 1:
            for i in range(1, len(graph[v])):
                next_vertex = graph[v][i]
                if graph[next_vertex] is not None:
                    if graph[next_vertex][0] is False:
                        # We are able to find an undiscovered vertex
                        # Put the current vertex on stack (in recursive version this means calling dfs again)
                        graph[next_vertex][0] = True
                        runtime_stack.append(v)
                        v = next_vertex
                        found = True
                        break
        if found:
            continue
        else:
            if phase == 1:
                topological_order_stack.append(v)
            else:
                size_of_scc += 1
            if len(runtime_stack) > 0:
                # We are not able to find any undiscovered vertices
                # But we have something on the stack. So backtrack ...
                v = runtime_stack.pop()
                continue
            else:
                # Nothing on the stack
                # The search is done
                break
    return -size_of_scc

def kusaraju():
    # Phase one
    v = max_vertex
    while v > 0:
        if graph_phase_one[v] is not None:
            if graph_phase_one[v][0] == False:
                dfs_iterative(v, 1)
        v -= 1
    # Phase two
    while len(topological_order_stack) > 0:
        v = topological_order_stack.pop()
        if graph_phase_two[v] is not None:
            if graph_phase_two[v][0] == False:
                heapq.heappush(scc_heap, dfs_iterative(v, 2))

if __name__ == '__main__':
    start_time = time.time()
    # Global data structures
    graph_phase_one = [None for x in range(0, 880000)]
    max_vertex = 0
    runtime_stack = []
    topological_order_stack = []
    graph_phase_two = [None for x in range(0, 880000)]
    scc_heap = []
    # Read input
    with open('C:\\testcases\\SCC.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            edge = line.strip().split()
            tail = int(edge[0])
            head = int(edge[1])
            max_vertex = max(tail, head, max_vertex)
            # Initialize data structures for phase one
            if graph_phase_one[head] is not None:
                graph_phase_one[head].append(tail)
            else:
                graph_phase_one[head] = [False, tail]
                max_vertex = max(head, max_vertex)
            if graph_phase_one[tail] is None:
                graph_phase_one[tail] = [False]
                max_vertex = max(tail, max_vertex)
            # Initialize data structures for phase two
            if graph_phase_two[tail] is not None:
                graph_phase_two[tail].append(head)
            else:
                graph_phase_two[tail] = [False, head]
            if graph_phase_two[head] is None:
                graph_phase_two[head] = [False]
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    # Start here
    kusaraju()
    # Output result
    result = [0 for x in range(0, 5)]
    for index in range(0, len(result)):
        if len(scc_heap) > 0:
            result[index] = -heapq.heappop(scc_heap)
        else:
            break
    print(result)
    print('Processing graph --- %s seconds ---' % (time.time() - start_time))