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
    # @return {integer[]}
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = [(root, False)]
        if root.right is not None:
            stack.append((root.right, True))
        if root.left is not None:
            stack.append((root.left, True))
        while stack:
            tup = stack.pop()
            if not tup[1]:
                result.append(tup[0].val)
            else:
                stack.append((tup[0], False))
                if tup[0].right is not None:
                    stack.append((tup[0].right, True))
                if tup[0].left is not None:
                    stack.append((tup[0].left, True))
        return result

if __name__ == '__main__':
    pass