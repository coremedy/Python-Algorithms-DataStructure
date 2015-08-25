'''
Created on 2015-08-25
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k <= 1:
            return head
        tmp_head, count, beg, lower_bound, end, upper_bound = head, 1, None, None, None, None
        while tmp_head:
            beg, end, upper_bound, tmp_head = beg if beg is not None else tmp_head, tmp_head, tmp_head.next, tmp_head.next
            if count == k:
                prev, tmp = upper_bound, beg
                while beg is not end:
                    beg.next, prev, beg = prev, beg, beg.next
                end.next = prev
                if lower_bound is None:
                    head = end
                else:
                    lower_bound.next = end
                count, lower_bound, beg, end, upper_bound = 1, tmp, None, None, None
            else:
                count = count + 1
        return head

if __name__ == '__main__':
    pass