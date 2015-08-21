'''
Created on 2015-08-20
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        if l1.val < l2.val:
            head, l1 = l1, l1.next
        else:
            head, l2 = l2, l2.next
        curr = head    
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, curr, l1 = l1, l1, l1.next
            else:
                curr.next, curr, l2 = l2, l2, l2.next
        if l1 is not None:
            curr.next = l1
        else:
            curr.next = l2
        return head

if __name__ == '__main__':
    pass