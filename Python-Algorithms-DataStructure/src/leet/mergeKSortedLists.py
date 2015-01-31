'''
Created on 2015-02-01
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        # The heap
        h = []
        result = None
        result_iter = None
        # Build the heap
        for head_node in lists:
            if head_node:
                heapq.heappush(h, (head_node.val, head_node.next))
        # Get the merge running
        while True:
            min_tup = None
            try:
                min_tup = heapq.heappop(h)
            except IndexError:
                break
            # We find the current minimal element
            # Build the result
            if result:
                result_iter.next = ListNode(min_tup[0])
                result_iter = result_iter.next
            else:
                result = ListNode(min_tup[0])
                result_iter = result
            # Look at next element
            if min_tup[1]:
                heapq.heappush(h, (min_tup[1].val, min_tup[1].next))
        # Return the result
        return result

if __name__ == '__main__':
    pass