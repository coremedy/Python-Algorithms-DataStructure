'''
Created on 2015-02-14

https://en.wikipedia.org/wiki/Tower_of_Hanoi
'''

import math

def path_calculator_backtrack(source, length):
    seq.append(source)
    # save the current sequence
    num = 0
    for i in range(length, -1, -1):
        num += seq[len(seq) - 1 - i] * int(math.pow(10, i))
    if num not in record:
        record[num] = length    
    hanio_graph_mask[source] = True
    for sibling in hanio_graph[source]:
        if hanio_graph_mask[sibling] == False:
            path_calculator_backtrack(sibling, length + 1)
    hanio_graph_mask[source] = False
    seq.pop()

if __name__ == '__main__':
    hanio_graph = [0, [2, 3], [1, 3, 4], [1, 2, 7], [2, 5, 6], [4, 6], [4, 5, 8], [3, 8, 9], [6, 7, 9], [7, 8]]
    hanio_graph_mask = [False, False, False, False, False, False, False, False, False, False]
    seq = []
    record = dict()
    path_calculator_backtrack(1, 0)