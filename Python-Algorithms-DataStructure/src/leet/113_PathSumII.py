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
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        result = []
        if root is None:
            return result
        self.BackTrack(root, 0, sum, [], result)
        return result
    
    def BackTrack(self, node, current_sum, sum, cache, result):
        if node.left is None and node.right is None:
            if current_sum + node.val == sum:
                result.append(cache + [node.val])
            return
        if node.left is not None:
            self.BackTrack(node.left, current_sum + node.val, sum, cache + [node.val], result)
        if node.right is not None:
            self.BackTrack(node.right, current_sum + node.val, sum, cache + [node.val], result)


if __name__ == '__main__':
    pass