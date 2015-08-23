'''
Created on 2015-08-23
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
        if head is None or head.next is None:
            return head
        tmp_head, removed, prev = head, False, None
        while tmp_head.next:
            if tmp_head.val == tmp_head.next.val:
                tmp_head.next, removed = tmp_head.next.next, True
            else:
                if removed:
                    if prev is None:
                        head = tmp_head.next 
                    else:
                        prev.next = tmp_head.next
                    removed = False
                else:
                    prev = tmp_head
                tmp_head = tmp_head.next
        if removed:
            if prev is None:
                head = tmp_head.next
            else:
                prev.next = tmp_head.next
        return head

if __name__ == '__main__':
    pass