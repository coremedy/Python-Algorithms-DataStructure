'''
Created on 2015-10-31
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        self.hit = False
        self.stop = False
        self.result = None
        self.dfs(root, p)
        return self.result

    def dfs(self, node, p):
        if node.left and not self.stop:
            self.dfs(node.left, p)
        if node is p:
            self.hit = True
        elif self.hit:
            self.result = node
            self.hit, self.stop = False, True
        if node.right and not self.stop:
            self.dfs(node.right, p)

if __name__ == '__main__':
    pass