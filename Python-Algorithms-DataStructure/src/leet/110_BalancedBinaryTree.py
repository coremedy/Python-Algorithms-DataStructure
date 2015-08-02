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
    # @return {boolean}
    def isBalanced(self, root):
        if root is None:
            return True
        result = [True]
        self.DFS(root, result)
        return result[0]
    
    def DFS(self, node, result):
        if not result[0]:
            return -1
        depth_left = 0
        if node.left is not None:
            depth_left = self.DFS(node.left, result)
        if not result[0]:
            return -1        
        depth_right = 0
        if node.right is not None:
            depth_right = self.DFS(node.right, result)
        if not result[0]:
            return -1
        if depth_left > depth_right:
            if depth_left - depth_right > 1:
                result[0] = False
                return -1
            return depth_left + 1
        else:
            if depth_right - depth_left > 1:
                result[0] = False
                return -1
            return depth_right + 1

if __name__ == '__main__':
    pass