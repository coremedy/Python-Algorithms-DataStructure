'''
Created on 2015-08-22
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        tmp_head, tmp_head_next = head, head.next
        tmp_head.next, tmp_head_next.next = tmp_head_next.next, tmp_head
        head, prev, tmp_head = tmp_head_next, tmp_head_next.next, tmp_head_next.next.next
        while tmp_head is not None and tmp_head.next is not None:
            tmp_head_next = tmp_head.next
            tmp_head.next, tmp_head_next.next = tmp_head_next.next, tmp_head
            prev.next, prev, tmp_head = tmp_head_next, tmp_head_next.next, tmp_head_next.next.next
        return head

if __name__ == '__main__':
    pass