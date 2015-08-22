'''
Created on 2015-08-21
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp_head, tmp_tail = head, head
        while n > 1:
            tmp_tail = tmp_tail.next
            n -= 1
        if tmp_tail.next is None:
            head = head.next
            return head
        prev = None
        while tmp_tail.next:
            prev, tmp_head, tmp_tail = tmp_head, tmp_head.next, tmp_tail.next
        prev.next = tmp_head.next
        return head

if __name__ == '__main__':
    pass