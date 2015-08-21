'''
Created on 2015-08-20
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        temp_head = head
        while temp_head.next.next:
            if temp_head.val == temp_head.next.val:
                temp_head.next = temp_head.next.next
            else:
                temp_head = temp_head.next
        if temp_head.val == temp_head.next.val:
            temp_head.next = None
        return head

if __name__ == '__main__':
    pass