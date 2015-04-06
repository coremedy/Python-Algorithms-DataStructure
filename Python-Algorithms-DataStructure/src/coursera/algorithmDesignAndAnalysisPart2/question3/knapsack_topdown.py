'''
Created on 2015-04-07

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=85
'''

import time
import sys

def knapsack_topdown(knapsack_size, item_index):
    # dirty version
    if item_index == 0:
        return 0
    
    if (knapsack_size, item_index) in record:
        return record[(knapsack_size, item_index)]
    
    item_value = items[item_index][0]
    item_weight = items[item_index][1]
    result = knapsack_topdown(knapsack_size, item_index - 1)
    
    if item_weight <= knapsack_size:
        temp_result = knapsack_topdown(knapsack_size - item_weight, item_index - 1) + item_value
        result = max(result, temp_result)
    
    record[(knapsack_size, item_index)] = result
    
    return result

if __name__ == '__main__':
    knapsack_size = 0
    number_of_items = 0
    start_time = time.time()
    items = [(-1, -1)]
    record = dict()
    # Read input
    first_line = True
    with open('C:\\testcases\\knapsack_big.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if first_line:
                knapsack_size = int(data[0])
                number_of_items = int(data[1])
                first_line = False
            else:
                # (value, weight)
                items.append((int(data[0]), int(data[1])))
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(old_limit * 100)
    print(knapsack_topdown(knapsack_size, number_of_items))
    sys.setrecursionlimit(old_limit)
    print('Dynamic programming --- %s seconds ---' % (time.time() - start_time))