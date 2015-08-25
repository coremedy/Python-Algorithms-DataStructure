'''
Created on 2015-08-25
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        recorder = dict()
        tmp_head, recorder[None] = head, None
        while tmp_head:
            recorder[tmp_head], tmp_head = RandomListNode(tmp_head.label), tmp_head.next
        result = recorder[head]
        result.random, tmp_head, tmp_result = recorder[head.random], head.next, result
        while tmp_head:
            tmp_result.next = recorder[tmp_head]
            tmp_result.next.random = recorder[tmp_head.random]
            tmp_head, tmp_result = tmp_head.next, tmp_result.next
        return result
    
if __name__ == '__main__':
    pass