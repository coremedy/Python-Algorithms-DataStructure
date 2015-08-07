'''
Created on 2015-08-07
'''

# Definition for a binary tree node.
# The original right nodes turned into left leaf nodes
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root):
        if root is None:
            return None
        result = []
        self.DFS(root, result)
        return result[0]
    
    def DFS(self, root, result):
        if root.left is None and root.right is None:
            if not result:
                result.append(root)
            return root
        left = self.DFS(root.left, result)
        right = None
        if root.right is not None:
            right = self.DFS(root.right, result)
        # Need to clean the pointers - or run into chaos
        root.left = root.right = None
        left.left = right
        left.right = root
        return root

if __name__ == '__main__':
    pass