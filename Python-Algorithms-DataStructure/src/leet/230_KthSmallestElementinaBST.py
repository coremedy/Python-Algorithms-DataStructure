'''
Created on 2015-08-06
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        count = [0]
        prev = [None]
        self.DFS(root, prev, count, k)
        return prev[0].val
    
    def DFS(self, root, prev, count, k):
        if root.left is not None:
            self.DFS(root.left, prev, count, k)
        if count[0] == k:
            return
        count[0] += 1
        prev[0] = root
        if count[0] == k:
            return
        if root.right is not None:
            self.DFS(root.right, prev, count, k)      

if __name__ == '__main__':
    pass