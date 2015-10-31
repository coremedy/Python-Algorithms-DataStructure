'''
Created on 2015-10-31
Consecutive means seq like 1,2,3,4 not 1,3,4
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = 0
        self.dfs(root, root, 1)
        return self.result
        
    def dfs(self, node, prev, length):
        if node.val == prev.val + 1:
            length += 1
        else:
            length = 1
        self.result = max(self.result, length)
        if node.left:
            self.dfs(node.left, node, length)
        if node.right:
            self.dfs(node.right, node, length)

if __name__ == '__main__':
    pass