'''
Created on 2015-08-25
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m < n:
            count, ptr_before_reversal, ptr_reversal_start = 1, None, head
            while count < m:
                ptr_before_reversal, ptr_reversal_start, count = ptr_reversal_start, ptr_reversal_start.next, count + 1
            tmp_ptr_reversal_start, prev = ptr_reversal_start, None
            while count <= n:
                ptr_reversal_start.next, ptr_reversal_start, prev, count = prev, ptr_reversal_start.next, ptr_reversal_start, count + 1
            if ptr_before_reversal is None:
                head = prev
            else:
                ptr_before_reversal.next = prev
            tmp_ptr_reversal_start.next = ptr_reversal_start
        return head

if __name__ == '__main__':
    pass