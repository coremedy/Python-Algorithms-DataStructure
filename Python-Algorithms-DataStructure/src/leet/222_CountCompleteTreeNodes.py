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
    def countNodes(self, root):
        if root is None:
            return 0
        left = root.left
        height_left = 0
        while left:
            height_left += 1
            left = left.left
        right = root.right
        height_right = 0
        while right:
            height_right += 1
            right = right.right
        if height_left == height_right:
            result = 1
            increment = 2
            for index in range(0, height_left):
                result += increment
                increment *= 2
            return result
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)           

if __name__ == '__main__':
    pass