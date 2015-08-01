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
    # @return {integer}
    def minDepth(self, root):
        result = 0
        if root is None:
            return 0
        nodes = [root]
        nodes_start = 0
        nodes_end = 1
        result += 1
        while True:
            found = False
            count = 0
            for index in range(nodes_start, nodes_end):
                if nodes[index].left is None and nodes[index].right is None:
                    found = True
                    break
                if nodes[index].left is not None:
                    count += 1
                    nodes.append(nodes[index].left)               
                if nodes[index].right is not None:
                    count += 1
                    nodes.append(nodes[index].right)
            if found:
                break
            result += 1
            nodes_start, nodes_end = nodes_end, nodes_end + count
        return result

if __name__ == '__main__':
    pass