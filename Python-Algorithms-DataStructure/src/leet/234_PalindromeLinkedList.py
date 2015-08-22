'''
Created on 2015-08-22
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        count = 1
        fast, slow = head, head 
        while fast.next:
            fast, slow, count = fast.next, slow.next, count + 1
            if fast.next:
                fast, count = fast.next, count + 1
        reversed_tail, reversed_head = slow if count % 2 == 0 else slow.next, fast
        prev = None
        while reversed_tail is not reversed_head:
            tmp = reversed_tail
            reversed_tail = reversed_tail.next
            tmp.next = prev
            prev = tmp
        reversed_head.next = prev
        count = count // 2
        while count > 0:
            if reversed_head.val != head.val:
                return False
            reversed_head, head, count = reversed_head.next, head.next, count - 1
        return True

if __name__ == '__main__':
    pass