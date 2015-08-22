'''
Created on 2015-08-22
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head, carry, l1, l2 = ListNode((l1.val + l2.val) % 10), (l1.val + l2.val) // 10, l1.next, l2.next
        result = head
        while l1 and l2:
            head.next = ListNode((l1.val + l2.val + carry) % 10)
            carry, l1, l2, head = (l1.val + l2.val + carry) // 10, l1.next, l2.next, head.next
        tail = l1 if l1 else l2
        while tail:
            head.next = ListNode((tail.val + carry) % 10)
            carry, head,tail   = (tail.val + carry) // 10, head.next, tail.next
        if carry > 0:
            head.next = ListNode(carry)
        return result

if __name__ == '__main__':
    pass