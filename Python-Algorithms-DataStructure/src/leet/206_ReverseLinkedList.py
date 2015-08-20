'''
Created on 2015-08-20
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = [None]
        if head:
            self.reverse(head, new_head)
        return new_head[0]
        
    def reverse(self, current, new_head):
        if current.next is None:
            new_head[0] = current
        else:
            self.reverse(current.next, new_head).next, current.next = current, None
        return current

if __name__ == '__main__':
    pass