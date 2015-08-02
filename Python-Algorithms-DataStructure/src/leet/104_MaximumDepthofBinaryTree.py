'''
Created on 2015-08-02
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        return self.DFS(0, root)

    def DFS(self, depth, node):
        if node is None:
            return depth
        return max(self.DFS(depth + 1, node.left), self.DFS(depth + 1, node.right))

if __name__ == '__main__':
    pass