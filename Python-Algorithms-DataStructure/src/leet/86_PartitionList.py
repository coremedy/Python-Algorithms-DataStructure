'''
Created on 2015-08-25
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        beg_left, end_left, beg_right, end_right = None, None, None, None
        while head:
            tmp = head.next
            if head.val < x:
                if end_left:
                    end_left.next = head
                end_left, head.next, beg_left = head, None, head if beg_left is None else beg_left
            else:
                if end_right:
                    end_right.next = head
                end_right, head.next, beg_right = head, None, head if beg_right is None else beg_right
            head = tmp
        if beg_left is not None:
            end_left.next = beg_right
            return beg_left
        else:
            return beg_right

if __name__ == '__main__':
    pass