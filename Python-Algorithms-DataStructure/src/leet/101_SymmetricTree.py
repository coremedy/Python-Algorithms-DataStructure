'''
Created on 2015-08-02
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        nodes = [root]
        current_level_count = 1
        while current_level_count > 0:
            for index in range(current_level_count):
                if nodes[index] is not None:
                    nodes.append(nodes[index].left)
                    nodes.append(nodes[index].right)
            start = 0
            end = current_level_count - 1
            while start < end:
                if nodes[start] is None and nodes[end] is None:
                    start += 1
                    end -= 1
                elif nodes[start] is not None and nodes[end] is not None:
                    if nodes[start].val != nodes[end].val:
                        return False
                    start += 1
                    end -= 1
                else:
                    return False
            nodes = nodes[current_level_count:]
            current_level_count = len(nodes)
        return True
    
    def DFS(self, left, right, result):
        if left is None and right is None:
            return
        elif left is not None and right is not None:
            if not result[0]:
                return
            if left.val != right.val:
                result[0] = False
                return
            self.DFS(left.left, right.right, result)
            if not result[0]:
                return
            self.DFS(left.right, right.left, result)
        else:
            result[0] = False

if __name__ == '__main__':
    pass