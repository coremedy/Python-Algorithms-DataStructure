'''
Created on 2015-08-07
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.populateStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        if not self.stack:
            return None
        elem = self.stack.pop()
        if not elem[1]:
            return elem[0].val
        self.populateStack(elem[0])
        return self.stack.pop()[0].val
        
    def populateStack(self, root):
        while root:
            if root.right is not None:
                self.stack.append((root.right, True))
            self.stack.append((root, False))
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    pass