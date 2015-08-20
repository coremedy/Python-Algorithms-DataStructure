'''
Created on 2015-08-20
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head is not None:
            current_node = head
            while current_node.next:
                if current_node.next.val == val:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
        return head

if __name__ == '__main__':
    pass