'''
Created on 2015-08-01
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        result = []
        if root is None:
            return result
        nodes = [root]
        nodes_start = 0
        nodes_end = 1
        reverse = False
        while True:
            count = 0
            tmp_result = []
            for index in range(nodes_start, nodes_end):
                if reverse:
                    tmp_result = [nodes[index].val] + tmp_result
                else:
                    tmp_result = tmp_result + [nodes[index].val]
                if nodes[index].left is not None:
                    nodes.append(nodes[index].left)
                    count += 1
                if nodes[index].right is not None:
                    nodes.append(nodes[index].right)
                    count += 1
            result.append(tmp_result)
            if count == 0:
                break
            nodes_start, nodes_end = nodes_end, nodes_end + count
            reverse = not reverse
        return result

if __name__ == '__main__':
    pass