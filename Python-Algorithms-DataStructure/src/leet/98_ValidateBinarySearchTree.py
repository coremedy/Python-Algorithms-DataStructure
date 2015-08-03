'''
Created on 2015-08-03
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
    def isValidBST(self, root):
        if root is None:
            return True
        result = [True]
        self.DFS(root, result)
        return result[0]
    
    def DFS(self, node, result):
        if node.left is None and node.right is None:
            return (node.val, node.val)
        elif node.left is not None and node.right is None:
            left_tuple = self.DFS(node.left, result)
            if not result[0]:
                return
            if left_tuple[1] >= node.val:
                result[0] = False
                return
            return (left_tuple[0], node.val)
        elif node.right is not None and node.left is None:
            right_tuple = self.DFS(node.right, result)
            if not result[0]:
                return
            if right_tuple[0] <= node.val:
                result[0] = False
                return
            return (node.val, right_tuple[1])
        else:
            left_tuple = self.DFS(node.left, result)
            if not result[0]:
                return            
            right_tuple = self.DFS(node.right, result)
            if not result[0]:
                return
            if left_tuple[1] >= node.val:
                result[0] = False
                return            
            if right_tuple[0] <= node.val:
                result[0] = False
                return
            return (left_tuple[0], right_tuple[1])

if __name__ == '__main__':
    pass