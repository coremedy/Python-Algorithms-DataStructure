'''
Created on 2015-08-04
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        current_root = TreeNode(nums[mid])
        current_root.left = self.sortedArrayToBST(nums[:mid])
        current_root.right = self.sortedArrayToBST(nums[mid + 1:])
        return current_root

if __name__ == '__main__':
    pass