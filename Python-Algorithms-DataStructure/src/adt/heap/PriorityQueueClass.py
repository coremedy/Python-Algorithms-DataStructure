'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import heapq

class PriorityQueue(object):
    def __init__(self):
        self.__queue = []
        # This is used to compare the items with same priority
        self.__index = 0
    
    def push(self, item, priority):
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        self.__index += 1
        
    def pop(self):
        return heapq.heappop(self.__queue)[-1]

class PriorityQueue_Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "PriorityQueue_Item({!r})".format(self.name)

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(PriorityQueue_Item('test1'), 1)
    q.push(PriorityQueue_Item('test2'), 4)
    q.push(PriorityQueue_Item('test3'), 3)
    assert(str(q.pop()) == "PriorityQueue_Item('test2')")
    print('Tests passed!'.center(20,'*'))