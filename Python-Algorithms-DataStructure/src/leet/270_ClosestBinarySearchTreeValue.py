'''
Created on 2015-10-18
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap, r = abs(root.val * 1.0 - target), root.val
        while root is not None:
            if abs(root.val * 1.0 - target) < gap:
                gap, r = abs(root.val * 1.0 - target), root.val
            root = root.left if (root.val * 1.0) > target else root.right
        return r

if __name__ == '__main__':
    pass