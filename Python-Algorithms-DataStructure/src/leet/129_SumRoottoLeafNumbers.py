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
    # @return {integer}
    def sumNumbers(self, root):
        if root is None:
            return 0
        result = [0]
        self.BackTrack(root, [], result)
        return result[0]
        
    def BackTrack(self, node, cache, result):
        if node.left is None and node.right is None:
            result[0] += int(''.join(cache + [chr(node.val + 48)]))
            return
        if node.left is not None:
            self.BackTrack(node.left, cache + [chr(node.val + 48)], result)
        if node.right is not None:
            self.BackTrack(node.right, cache + [chr(node.val + 48)], result)

if __name__ == '__main__':
    pass