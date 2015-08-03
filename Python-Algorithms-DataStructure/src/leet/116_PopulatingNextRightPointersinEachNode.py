'''
Created on 2015-08-03
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is not None:
            if root.left is not None and root.right is not None:
                # Pre-Order
                root.left.next = root.right
                next_root = root.next
                if next_root is not None:
                    root.right.next = next_root.left
                self.connect(root.left)
                self.connect(root.right)

if __name__ == '__main__':
    pass