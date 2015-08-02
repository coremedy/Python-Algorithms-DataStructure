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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        result = [False]
        self.DFS(root, 0, result, sum)
        return result[0]
    
    def DFS(self, node, current_sum, result, sum):
        if node.left is None and node.right is None:
            if current_sum + node.val == sum:
                result[0] = True
            return
        if node.left is not None:
            if result[0]:
                return
            self.DFS(node.left, current_sum + node.val, result, sum)
        if node.right is not None:
            if result[0]:
                return
            self.DFS(node.right, current_sum + node.val, result, sum)

if __name__ == '__main__':
    pass