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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if not root:
            return self.result
        self.dfs(root, [])
        return self.result

    def dfs(self, node, values):
        if not node.left and not node.right:
            self.result.append('->'.join(values + [str(node.val)]))
            return
        if node.left:
            self.dfs(node.left, values + [str(node.val)])
        if node.right:
            self.dfs(node.right, values + [str(node.val)])

if __name__ == '__main__':
    pass