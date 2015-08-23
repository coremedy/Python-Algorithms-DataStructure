'''
Created on 2015-08-23
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        length, beg = 0, head
        while beg:
            length, beg = length + 1, beg.next
        k = k % length
        if k == 0:
            return head
        count, beg, end = k - 1, head, head
        while count > 0 and end.next:
            count, end = count - 1, end.next
        if end.next is None:
            return beg
        prev = None
        while end.next:
            prev, beg, end = beg, beg.next, end.next
        end.next, prev.next = head, None
        return beg

if __name__ == '__main__':
    pass