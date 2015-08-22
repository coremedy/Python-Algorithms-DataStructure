'''
Created on 2015-08-22
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast, slow = head, head
        while True:
            fast, slow = fast.next, slow.next
            if fast:
                fast = fast.next
            if fast is None or slow is None:
                break
            if fast is slow:
                return True
        return False

if __name__ == '__main__':
    pass