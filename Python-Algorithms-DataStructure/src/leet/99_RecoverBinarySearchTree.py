'''
Created on 2015-08-05

When you use in-order traversal, the tree becomes a sorted array.
Then how to find reversed pair in sorted array? You need to know previous element and current element.
Condition 1: 1235467 - 54 is reversed and you need to swap them
Condition 2: 1634527 - 62 is reversed, and there are two pairs, 63 and 52, you need to swap 6 and 2
For constant space requirement, you need to use Morris Traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        bookmark = []
        prevNode = [None]
        self.DFS_INORDER(root, prevNode, bookmark)
        if len(bookmark) == 2:
            bookmark[0].val, bookmark[1].val = bookmark[1].val, bookmark[0].val
        elif len(bookmark) == 4:
            bookmark[0].val, bookmark[3].val = bookmark[3].val, bookmark[0].val
    
    def DFS_INORDER(self, root, prevNode, bookmark):
        if root is None:
            return
        if root.left is not None:
            self.DFS_INORDER(root.left, prevNode, bookmark)
        if prevNode[0] is not None:
            if len(bookmark) == 0 and prevNode[0].val > root.val:
                bookmark.append(prevNode[0])
                bookmark.append(root)
            elif len(bookmark) == 2 and prevNode[0].val > root.val:
                bookmark.append(prevNode[0])
                bookmark.append(root)
                return
        prevNode[0] = root
        if root.right is not None:
            self.DFS_INORDER(root.right, prevNode, bookmark)
   

if __name__ == '__main__':
    pass