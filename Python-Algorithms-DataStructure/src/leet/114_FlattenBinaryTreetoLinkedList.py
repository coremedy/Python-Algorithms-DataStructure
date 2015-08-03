'''
Created on 2015-08-03
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        self.DFS(root)
        return
    
    def DFS(self, root):
        if root is not None:
            if root.left is None and root.right is None:
                return (root, root)
            elif root.left is not None and root.right is None:
                left_tuple = self.DFS(root.left)
                root.right = left_tuple[0]
                root.left = None
                return (root, left_tuple[1])
            elif root.left is None and root.right is not None:
                right_tuple = self.DFS(root.right)
                return (root, right_tuple[1])
            else:
                left_tuple = self.DFS(root.left)
                right_tuple = self.DFS(root.right)
                root.left = None
                root.right = left_tuple[0]
                left_tuple[1].right = right_tuple[0]
                return (root, right_tuple[1])

if __name__ == '__main__':
    pass