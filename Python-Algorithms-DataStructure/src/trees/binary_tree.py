'''
Created on 2014-12-24

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import random
import sys

class NodeBT(object):
    def __init__(self, item, depth = 0):
        self.item = item
        self.depth = depth
        self.left = None
        self.right = None
    
    def __repr__(self, *args, **kwargs):
        return '{}'.format(self.item)
        
    def _isLeaf(self):
        return (not self.right) and (not self.left)
    
    '''
    Get max height of the current node
    rootNode._getMaxHeight == leafNode.depth
    '''
    def _getMaxHeight(self):
        levelr, levell = 0, 0
        if self.right:
            levelr = self.right._getMaxHeight() + 1
        if self.left:
            levell = self.left._getMaxHeight() + 1
        return max(levelr, levell)
    
    def _getMinHeight(self):
        levelr, levell = -1, -1
        if self.right:
            levelr = self.right._getMinHeight()
        if self.left:
            levell = self.left._getMinHeight()
        return min(levelr, levell) + 1

    def _addNextNode(self, item):
        # without left sub-tree
        if (not self.left) and (self.right):
            self.left = NodeBT(item, self.depth + 1)
            return self.left
        # without right sub-tree
        if (not self.right) and (self.left):
            self.right = NodeBT(item, self.depth + 1)
            return self.right
        if random.randint(0, 1) == 0:
            # left sub-tree
            if not self.left:
                self.left = NodeBT(item, self.depth + 1)
                return self.left
            else:
                return self.left._addNextNode(item)
        else:
            # right sub-tree
            if not self.right:
                self.right = NodeBT(item, self.depth + 1)
                return self.right
            else:
                return self.right._addNextNode(item)
    
    def _searchForNode(self, value):
        if self.item == value:
            return self
        found = None
        if self.left:
            found = self.left._searchForNode(value)
        if self.right:
            found = found or self.right._searchForNode(value)
        return found
    
    def _isBalanced(self):
        if self._getMaxHeight() - self._getMinHeight() < 2:
            return True
        return False

    def _isBST(self, min_item = -sys.maxsize, max_item = sys.maxsize):
        if not self.item:
            print("The item of this node is empty!")
            return False
        if (self.item > max_item) or (self.item < min_item):
            return False
        if self._isLeaf():
            return True
        elif self.left and (not self.right):
            return self.left._isBST(min_item, self.item)
        elif self.right and (not self.left):
            return self.right._isBST(self.item, max_item)
        else:
            return self.left._isBST(min_item, self.item) and self.right._isBST(self.item, max_item)

class BinaryTree(object):
    def __init__(self):
        self.root = None
        
    def addNode(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._addNextNode(value)
    
    def isLeaf(self, value):
        node = self.root._searchForNode(value)
        return node._isLeaf()
    
    def getNodeDepth(self, item):
        node = self.root._searchForNode(item)
        if node:
            return node.depth
        else:
            raise Exception('Node not found')
        
    def isRoot(self, value):
        return self.root.item == value

    def getHeight(self):
        return self.root._getMaxHeight()

    def isBalanced(self):
        return self.root._isBalanced()
    
    def isBST(self):
        return self.root._isBST()

if __name__ == '__main__':
    bt = BinaryTree()
    print("Adding nodes 1 to 10 in the tree...")
    for i in range(1, 10):
        bt.addNode(i)
    print ("Is 8 a leaf? ", bt.isLeaf(8))
    print ("Whats the level of node 8? ", bt.getNodeDepth(8))
    print ("Is node 10 a root? ", bt.isRoot(10))
    print ("Is node 1 a root? ", bt.isRoot(1))
    print ("Whats the tree height? ", bt.getHeight())
    print ("Is this tree BST? ", bt.isBST())
    print ("Is this tree balanced? ", bt.isBalanced())