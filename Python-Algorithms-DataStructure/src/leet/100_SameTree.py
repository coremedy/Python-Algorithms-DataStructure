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
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            result = [True]
            self.DFS(p, q, result)
            return result[0]
        else:
            return False
            
    def DFS(self, p, q, result):
        if p.val != q.val:
            result[0] = False
            return
        if p.left is None and q.left is None:
            pass
        elif p.left is not None and q.left is not None:
            if result[0]:
                self.DFS(p.left, q.left, result)
        else:
            result[0] = False
            return            
        if p.right is None and q.right is None:
            pass
        elif p.right is not None and q.right is not None:
            if result[0]:
                self.DFS(p.right, q.right, result)
        else:
            result[0] = False
            return

if __name__ == '__main__':
    pass