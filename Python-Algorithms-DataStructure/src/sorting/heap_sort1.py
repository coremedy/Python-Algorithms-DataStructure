'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import heapq

def heap_sort1(seq):
    h = []
    for val in seq:
        heapq.heappush(h, val)
    return [heapq.heappop(h) for i in range(len(seq))]

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(heap_sort1(seq) == sorted(seq))
    print('Tests passed!')