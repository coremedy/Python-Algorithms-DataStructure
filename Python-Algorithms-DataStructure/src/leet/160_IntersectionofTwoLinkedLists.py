'''
Created on 2015-08-20
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        A_length, B_length = 0, 0
        temp_headA, temp_headB  = headA, headB
        while temp_headA or temp_headB:
            if temp_headA:
                temp_headA = temp_headA.next
                A_length += 1
            if temp_headB:
                temp_headB = temp_headB.next
                B_length += 1
        difference = 0
        if A_length > B_length:
            difference = A_length - B_length
            while difference > 0:
                headA = headA.next
                difference -= 1
        elif A_length < B_length:
            difference = B_length - A_length 
            while difference > 0:
                headB = headB.next
                difference -= 1
        while headA and headB:
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

if __name__ == '__main__':
    pass