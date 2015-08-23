'''
Created on 2015-08-23
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy_head = ListNode(0)
        dummy_head.next, curr = head, head
        while curr.next:
            if curr.next.val >= curr.val:
                curr = curr.next
            else:
                prev = dummy_head
                while prev.next.val < curr.next.val:
                    prev = prev.next
                tmp, curr.next = curr.next, curr.next.next
                tmp.next, prev.next = prev.next, tmp
        return dummy_head.next
    
    def insertionSortList_raw(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        new_head, head = head, head.next
        new_head.next = None
        while head:
            tmp, head.next = head.next, None
            new_head, head = self.insertElement(new_head, head), tmp
        return new_head

    def insertElement(self, new_head, elem):
        if elem.val <= new_head.val:
            elem.next, new_head = new_head, elem
            return new_head
        else:
            prev, tmp_head = new_head, new_head.next
            while tmp_head:
                if tmp_head.val >= elem.val:
                    prev.next, elem.next = elem, tmp_head
                    return new_head
                else:
                    prev, tmp_head = tmp_head, tmp_head.next
            if not tmp_head:
                prev.next = elem
            return new_head

if __name__ == '__main__':
    pass