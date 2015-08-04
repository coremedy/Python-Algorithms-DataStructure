'''
Created on 2015-08-04
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        prev_ptr, curr_ptr, fast_ptr = None, head, head
        while True:
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.next
            # Need to use fast-runner, introduced in CC150
            fast_ptr = fast_ptr.next
            if fast_ptr.next is None:
                break
            fast_ptr = fast_ptr.next
            if fast_ptr.next is None:
                break
        current_node = TreeNode(curr_ptr.val)
        prev_ptr.next = None
        current_node.left = self.sortedListToBST(head)
        current_node.right = self.sortedListToBST(curr_ptr.next)
        return current_node

if __name__ == '__main__':
    pass