'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import heapq

if __name__ == '__main__':
    heap = []
    '''
    The heapq documentation suggests that heap elements could be tuples in which the first element is the priority and defines the sort order.
    '''
    heapq.heappush(heap, (1, 'food'))
    heapq.heappush(heap, (2, 'study'))
    heapq.heappush(heap, (3, 'work'))
    heapq.heappush(heap, (4, 'have fun'))
    
    print(heap)
    print(heapq.heappop(heap))
    print(heap)
    heapq.heappush(heap, (2.5, 'have fun'))
    print(heap)
    '''
    Merge multiple sorted inputs into a single sorted output
    '''
    for i in heapq.merge([1,3,5], [2,4,6]):
        print(i)
        
    print(4 and 3)
    