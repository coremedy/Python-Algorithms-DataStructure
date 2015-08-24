'''
Created on 2015-08-23
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not (head is None or head.next is None or head.next.next is None):
            count, fast, slow, prev = 1, head, head, None
            while fast.next:
                prev, count, fast, slow = slow, count + 1, fast.next, slow.next
                if fast.next:
                    count, fast = count + 1, fast.next
            if count % 2 == 0:
                prev.next = None
            else:
                slow.next, slow = None, slow.next
            prev = None
            while slow is not fast:
                slow.next, prev, slow = prev, slow, slow.next
            fast.next = prev
            count = count // 2
            while count > 0:
                head.next, fast.next, head, fast, count = fast, head.next, head.next, fast.next, count - 1

if __name__ == '__main__':
    pass
