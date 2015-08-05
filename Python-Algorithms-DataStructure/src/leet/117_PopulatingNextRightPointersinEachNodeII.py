'''
Created on 2015-08-05
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
        if root is None:
            return
        # From right to left, or the chain will be broken
        if root.right is not None:
            next_root = root.next
            target = None
            while next_root is not None:
                target = next_root.left
                if target is not None:
                    break
                target = next_root.right
                if target is not None:
                    break
                next_root = next_root.next
            root.right.next = target
        if root.right is not None:
            self.connect(root.right)
        # Now we can process the left
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
            else:
                next_root = root.next
                target = None
                while next_root is not None:
                    target = next_root.left
                    if target is not None:
                        break
                    target = next_root.right
                    if target is not None:
                        break
                    next_root = next_root.next
                root.left.next = target
        if root.left is not None:
            self.connect(root.left)

if __name__ == '__main__':
    pass
