'''
Created on 2015-08-06
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        if p.left is q or p.right is q:
            return p
        if q.left is p or q.right is p:
            return q
        result_sequences = []
        self.DFS(root, p, q, result_sequences, [])
        prev = root
        length = min(len(result_sequences[0]), len(result_sequences[1]))
        for index in range(1, length):
            if result_sequences[0][index] is not result_sequences[1][index]:
                break
            else:
                prev = result_sequences[0][index]
        return prev
        
    def DFS(self, root, p, q, result_sequences, cache):
        if root is p:
            result_sequences.append(cache + [p])
            if len(result_sequences) == 2:
                return
        if root is q:
            result_sequences.append(cache + [q])
            if len(result_sequences) == 2:
                return
        if root.left is not None:
            self.DFS(root.left, p, q, result_sequences, cache + [root])
        if len(result_sequences) == 2:
            return
        if root.right is not None:
            self.DFS(root.right, p, q, result_sequences, cache + [root])

if __name__ == '__main__':
    pass