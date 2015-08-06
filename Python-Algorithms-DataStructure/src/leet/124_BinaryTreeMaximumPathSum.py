'''
Created on 2015-08-06
Divide and Conquer
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
    def maxPathSum(self, root):
        if root is None:
            return 0
        result_tup = self.DFS(root)
        return result_tup[0]
    
    def DFS(self, root):
        if root.left is None and root.right is None:
            return (root.val, root.val)
        elif root.left is not None and root.right is None:
            left_tuple = self.DFS(root.left)
            return (max(left_tuple[0], root.val, left_tuple[1] + root.val), max(left_tuple[1] + root.val, root.val))
        elif root.left is None and root.right is not None:
            right_tuple = self.DFS(root.right)
            return (max(right_tuple[0], root.val, right_tuple[1] + root.val), max(right_tuple[1] + root.val, root.val))
        else:
            left_tuple = self.DFS(root.left)
            right_tuple = self.DFS(root.right)
            return (max(left_tuple[0], right_tuple[0], root.val, left_tuple[1] + root.val, right_tuple[1] + root.val, left_tuple[1] + root.val + right_tuple[1]), max(left_tuple[1] + root.val, right_tuple[1] + root.val, root.val))

if __name__ == '__main__':
    pass