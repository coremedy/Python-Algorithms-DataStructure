'''
Created on 2015-04-21

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=93
'''

import time
import math
import itertools
import functools
import numpy

def bit_count(u):
    u_count = u - ((u >> 1) & 0o33333333333) - ((u >> 2) & 0o11111111111);
    return ((u_count + (u_count >> 3)) & 0o30707070707) % 63

def construct_binary_repr(tup):
    result = 0
    for bit in tup:
        result |= 1 << (bit - 1)
    return result

if __name__ == '__main__':
    start_time = time.time()
    bit_index_to_coordination = [(-1, -1)]
    with open('C:\\testcases\\tsp.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 1:
                number_of_cities = int(data[0])
                distance_matrix = [[0 for dummy_col in range(0, number_of_cities + 1)] for dummy_row in range(0, number_of_cities + 1)]
            else:
                bit_index_to_coordination.append((float(data[0]), float(data[1])))
    for outer_city in range(1, number_of_cities):
        for inner_city in range(outer_city + 1, number_of_cities + 1):
            dist = math.sqrt(math.pow(bit_index_to_coordination[outer_city][0] - bit_index_to_coordination[inner_city][0], 2) + math.pow(bit_index_to_coordination[outer_city][1] - bit_index_to_coordination[inner_city][1], 2))
            distance_matrix[outer_city][inner_city] = distance_matrix[inner_city][outer_city] = dist
    length_set_map = dict()
    for length in range(1, number_of_cities + 1):
        length_set_map[length] = filter(lambda tup: tup[0] == 1, itertools.combinations([dummy_row for dummy_row in range(1, number_of_cities + 1)], length))
    dynamic_programming_table = numpy.zeros((int(math.pow(2, number_of_cities)), number_of_cities + 1), float)    
    print('Processing input and creating data structure: --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    for m in range(2, number_of_cities + 1):
        start_time2 = time.time()
        for each_set in length_set_map[m]:
            for j in each_set[1:]:
                binary_repr_S = functools.reduce(lambda x, y : x + (1 << (y - 1)), each_set)
                min_val = float('inf')
                for k in filter(lambda z: z != j, each_set):
                    binary_repr_S_minus_j = binary_repr_S ^ (1 << (j - 1))
                    if k != 1:
                        min_val = min(min_val, dynamic_programming_table[binary_repr_S_minus_j][k] + distance_matrix[k][j])
                    else:
                        if binary_repr_S_minus_j == 1:
                            min_val = min(min_val, distance_matrix[k][j])
                dynamic_programming_table[binary_repr_S][j] = min_val
        print('Processing length %s: --- %s seconds ---' % (m, (time.time() - start_time2)))
    final_val = dynamic_programming_table[int(math.pow(2, number_of_cities)) - 1][2] +  distance_matrix[2][1]
    for j in range(3, number_of_cities + 1):
        final_val = min(final_val, dynamic_programming_table[int(math.pow(2, number_of_cities)) - 1][j] +  distance_matrix[j][1])
    print(int(final_val))
    print('Dynamic programming: --- %s seconds ---' % (time.time() - start_time))