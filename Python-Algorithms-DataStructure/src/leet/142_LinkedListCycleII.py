'''
Created on 2015-08-23
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow, fast = head, head
        while True:
            slow, fast = slow.next, fast.next
            if fast.next is None:
                break
            fast = fast.next
            if fast.next is None or slow is fast:
                break
        if fast.next is None:
            return None
        if slow is head:
            return slow
        slow = head
        while slow is not fast:
            slow, fast = slow.next, fast.next
        return fast

if __name__ == '__main__':
    pass