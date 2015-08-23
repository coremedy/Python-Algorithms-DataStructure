'''
Created on 2015-08-23
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        end = head
        while end.next:
            end = end.next
        return self.mergeSort(head, end)

    def mergeSort(self, beg, end):
        if beg is end:
            beg.next = None
            return beg
        left_end, right_beg, right_end = None, beg, beg
        while True:
            left_end, right_beg, right_end = right_beg, right_beg.next, right_end.next
            if right_end is end:
                break
            right_end = right_end.next
            if right_end is end:
                break
        left = self.mergeSort(beg, left_end)
        right = self.mergeSort(right_beg, right_end)
        head = None
        if left.val < right.val:
            head, left = left, left.next
        else:
            head, right = right, right.next
        result = head
        while left and right:
            if left.val < right.val:
                head.next, head, left = left, left, left.next 
            else:
                head.next, head, right = right, right, right.next
        if left:
            head.next = left
        else:
            head.next = right
        return result

if __name__ == '__main__':
    pass