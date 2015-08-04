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

    def DFS(self, preorder, preorder_beg, preorder_end, inorder, inorder_beg, inorder_end):
        if preorder_beg > preorder_end or inorder_beg > inorder_end:
            return None
        key = preorder[preorder_beg]
        index = self.BruteForceSearch(inorder, inorder_beg, inorder_end, key)
        node = TreeNode(key)
        node.left = self.DFS(preorder, preorder_beg + 1, preorder_beg + index - inorder_beg, inorder, inorder_beg, index - 1)
        node.right = self.DFS(preorder, preorder_end + 1 + index - inorder_end, preorder_end, inorder, index + 1, inorder_end)
        return node
        
    def BruteForceSearch(self, array, beg, end, key):
        for index in range(beg, end + 1):
            if array[index] == key:
                return index
        return -1

if __name__ == '__main__':
    pass