'''
Created on 2015-08-04
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        # Tricky
        root = preorder.pop(0)
        index = inorder.index(root)
        node = TreeNode(root)
        node.left = self.buildTree(preorder, inorder[:index])
        # Only nodes from right subtree reside in preorder array
        node.right = self.buildTree(preorder, inorder[index + 1:])
        return node

if __name__ == '__main__':
    pass