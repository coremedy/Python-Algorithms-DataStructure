'''
Created on 2014-12-30
Code coming from: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
'''

import sys

class TreeNode(object):
    
    def __init__(self, key, val, left = None, right = None, parent = None, depth = 0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.depth = depth
        # only root node does not have parent
        self.parent = parent
        # This is okay because the balance factor of a leaf is zero
        self.balanceFactor = 0
    
    def hasLeftChild(self):
        # None or left child
        return self.leftChild
    
    def hasRightChild(self):
        # None or right child
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and (self.parent.leftChild is self)
    
    def isRightChild(self):
        return self.parent and (self.parent.rightChild is self)

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def getDepth(self):
        return self.depth

    def adjustDepth(self, depth):
        # pre-order
        self.depth = depth
        if self.leftChild:
            self.leftChild.adjustDepth(depth + 1)
        if self.rightChild:
            self.rightChild.adjustDepth(depth + 1)

    # additional functions
    def getHeight(self, minHeight = False):
        mh_left, mh_right = -1, -1
        if self.leftChild:
            mh_left = self.leftChild.getMinimumHeight(minHeight)
        if self.rightChild:
            mh_right = self.rightChild.getMinimumHeight(minHeight)
        if minHeight:
            return min(mh_left, mh_right) + 1
        else:
            return max(mh_left, mh_right) + 1
    
    def isBalanced(self):
        if self.getHeight() - self.getHeight(True) < 2:
            return True
        return False
    
    def isBST(self, min_key = -sys.maxsize, max_key = sys.maxsize):
        if not self.key:
            print("The key of this node is empty!")
            return False
        if (self.key > max_key) or (self.key < min_key):
            return False
        if self.isLeaf():
            return True
        elif self.leftChild and (not self.rightChild):
            return self.leftChild.isBST(min_key, self.key)
        elif self.rightChild and (not self.leftChild):
            return self.rightChild.isBST(self.key, min_key)
        else:
            return self.leftChild.isBST(min_key, self.key) and self.rightChild.isBST(self.key, max_key)