'''
Created on 2015-02-06

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=52
Random choice procedure comes from: https://code.activestate.com/recipes/577363-weighted-random-choice/
Algorithm comes from paper: An O(n^2) Algorithm for Minimum Cuts by David R. Karger and Clifford Stein
'''

import math
import random
import bisect

def weighted_random_choice(seq, adjacent_matrix, u):
    weights = 0
    elems = []
    for elem in seq:
        w = adjacent_matrix[u][elem]  
        try:
            is_neg = w < 0
        except TypeError:
            raise ValueError("Weight of element '%s' is not a number (%s)" % (elem, w))
        if is_neg:
            raise ValueError("Weight of element '%s' is negative (%s)" % (elem, w))
        if w != 0:
            try:
                weights += w
            except TypeError:
                raise ValueError("Weight of element '%s' is not a number (%s)" % (elem, w))
            elems.append((weights, elem))
    if not elems:
        raise ValueError("Empty sequence")
    ix = bisect.bisect(elems, (random.uniform(0, weights), None))
    return elems[ix][1]

def karger_mincut(adjacent_matrix, vertice_set, adjacent_table):
    # O(n) iterations
    while len(vertice_set) > 2:
        # Get the random edge - O(n)
        # If you don't use this approach, you will only get a result of 20, which is not correct
        # Choose with WEIGHT S(vertex)
        u = weighted_random_choice(vertice_set, adjacent_matrix, 0)
        # Choose with WEIGHT W(u, vertex)
        v = weighted_random_choice(vertice_set.difference(set([u])).intersection(adjacent_table[u]), adjacent_matrix, u)
        # Start working on matrix - O(n)
        adjacent_matrix[0][u] = adjacent_matrix[0][u] + adjacent_matrix[0][v] - 2 * adjacent_matrix[u][v]
        adjacent_matrix[u][0] = adjacent_matrix[u][0] + adjacent_matrix[v][0] - 2 * adjacent_matrix[u][v]
        adjacent_matrix[0][v] = adjacent_matrix[v][0] = 0
        adjacent_matrix[u][v] = adjacent_matrix[v][u] = 0
        for vertex in adjacent_table[u].union(adjacent_table[v]).difference(set([u, v])):
            adjacent_matrix[u][vertex] += adjacent_matrix[v][vertex]
            adjacent_matrix[vertex][u] += adjacent_matrix[vertex][v]
            adjacent_matrix[v][vertex] = 0
            adjacent_matrix[vertex][v] = 0
        vertice_set.discard(v)
        # Start working on adjacent table - O(n)
        adjacent_table[u].remove(v)
        adjacent_table[v].remove(u)
        adjacent_table[u].update(adjacent_table[v])
        adjacent_table.pop(v)
        for key in adjacent_table.keys():
            if v in adjacent_table[key]:
                adjacent_table[key].remove(v)
                adjacent_table[key].add(u)        
    return adjacent_matrix[vertice_set.pop()][vertice_set.pop()]

if __name__ == '__main__':
    # There are 200 vertices labeled 1 to 200.
    # This implies adjacent matrix is a good choice
    adjacent_matrix_global = [[0 for y in range(0, 256)] for x in range(0, 256)]
    vertice_set_global = set()
    # Build local copy
    adjacent_matrix_runtime = [[0 for y in range(0, 256)] for x in range(0, 256)]
    vertice_set_runtime = set()
    # Get the input
    with open('C:\\testcases\\kargerMinCut.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            vertice = line.strip().split()
            vertice_set_global.add(int(vertice[0]))
            S = 0
            for i in range(1, len(vertice)):
                S += 1
                adjacent_matrix_global[int(vertice[0])][int(vertice[i])] = 1
            adjacent_matrix_global[int(vertice[0])][0] = adjacent_matrix_global[0][int(vertice[0])] = S
    # Since this is random algorithm, we need it to run for O(n^2logn) times to get the success rate of (1 - 1/n)
    # However, you will soon discover the correct result after hundreds of execution and then please kill the program
    # Overall, O(n^4logn)
    execution_times = len(vertice_set_global) * len(vertice_set_global) * int(math.log2(len(vertice_set_global)))
    minimal_cut = len(vertice_set_global)
    count = 0
    while execution_times > 0:
        # Initialize local copy
        adjacent_table = dict()
        for x in vertice_set_global:
            vertice_set_runtime.add(x)
            adjacent_table[x] = set()
        # O(n^2)
        for i in range(0, max(vertice_set_global) + 1):
            for j in range(0, max(vertice_set_global) + 1):
                adjacent_matrix_runtime[i][j] = adjacent_matrix_global[i][j]
                if (i != 0) and (j != 0) and (adjacent_matrix_global[i][j] > 0):
                    adjacent_table[i].add(j)
        # O(n^2)
        minimal_cut = min(minimal_cut, karger_mincut(adjacent_matrix_runtime, vertice_set_runtime, adjacent_table))
        execution_times -= 1
        count += 1
        print("Executed %d times, the current result is %d " % (count, minimal_cut))
    
    print("Final result is: %d" % (minimal_cut))