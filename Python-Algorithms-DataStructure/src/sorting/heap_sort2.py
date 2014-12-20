'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.heap.heapify import Heapify

def heap_sort2(seq):
    h = Heapify(seq)
    res = [h.extract_max() for i in range(len(seq))]
    return list(reversed(res))

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(heap_sort2(seq) == sorted([3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]))
    print('Tests passed!')