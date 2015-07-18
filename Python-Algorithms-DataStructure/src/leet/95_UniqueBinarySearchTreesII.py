'''
Created on 2015-07-18

DP table
                      [1|2|3|4|5]
                [1|2|3|4]    [2|3|4|5]
          [1|2|3]     [2|3|4]      [3|4|5]
      [1|2]      [2|3]       [3|4]        [4|5]
   [1]      [2]        [3]          [4]        [5]

'{1,#,2,3}' can be used instead of actual tree nodes
But in the end we still need to construct the tree
Use dfs here
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.dfs(1, n)
        
    def dfs(self, start_node, end_node):
        # Baseline
        if start_node > end_node:
            return [None]
        result = []
        for elem in range(start_node, end_node + 1):
            left_subtree_list = self.dfs(start_node, elem - 1)
            right_subtree_list = self.dfs(elem + 1, end_node)
            for left_subtree in left_subtree_list:
                for right_subtree in right_subtree_list:
                    new_node = TreeNode(elem)
                    new_node.left = left_subtree
                    new_node.right = right_subtree
                    result.append(new_node)
        return result

if __name__ == '__main__':
    pass