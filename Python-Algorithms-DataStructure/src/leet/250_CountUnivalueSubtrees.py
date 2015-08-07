'''
Created on 2015-08-07
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
    def countUnivalSubtrees(self, root):
        result = [0]
        if root is None:
            return result[0]
        self.DFS(root, result)
        return result[0]
        
    def DFS(self, root, result):
        if root.left is None and root.right is None:
            result[0] += 1
            return True
        result_from_left = True
        if root.left is not None:
            if not (self.DFS(root.left, result) and root.left.val == root.val):
                result_from_left = False
        result_from_right = True
        if root.right is not None:
            if not (self.DFS(root.right, result) and root.right.val == root.val):
                result_from_right = False       
        if result_from_right and result_from_left:
            result[0] += 1
            return True
        return False

if __name__ == '__main__':
    pass