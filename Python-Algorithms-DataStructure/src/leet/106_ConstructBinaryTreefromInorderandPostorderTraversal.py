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
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = postorder.pop()
        index = inorder.index(root)
        node = TreeNode(root)
        node.right = self.buildTree(inorder[index + 1:], postorder)
        node.left = self.buildTree(inorder[:index], postorder)
        return node

if __name__ == '__main__':
    pass