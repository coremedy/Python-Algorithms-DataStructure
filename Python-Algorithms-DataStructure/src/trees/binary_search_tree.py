'''
Created on 2014-12-25

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from trees.binary_tree import NodeBT, BinaryTree

class NodeBST(NodeBT):
    
    def __init__(self, item, depth = 0):
        super(NodeBST, self).__init__(item, depth)
        
    def _addNextNode(self, item):
        if item < self.item:
            if self.left:
                return self.left._addNextNode(item)
            else:
                self.left = NodeBST(item, self.depth + 1)
                return self.left
        elif item > self.item:
            if self.right:
                return self.right._addNextNode(item)
            else:
                self.right = NodeBST(item, self.depth + 1)
                return self.right
        else:
            print("BSTs do not support repeated items.")
            return None
    
    def _searchForNode(self, value):
        if self.item == value:
            return self
        elif self.left and value < self.item:
            return self.left._searchForNode(value)
        elif self.right and value > self.item:
            return self.right._searchForNode(value)
        return None

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._addNextNode(value)

if __name__ == '__main__':
    bst = BinarySearchTree()
    print("Adding nodes 1 to 10 in the tree...")
    for i in range(1, 10):
        bst.addNode(i)
    print("Is 8 a leaf? ", bst.isLeaf(8))
    print("Whats the level of node 8? ", bst.getNodeDepth(8))
    print("Is node 10 a root? ", bst.isRoot(10))
    print("Is node 1 a root? ", bst.isRoot(1))
    print("Whats the tree height? ", bst.getHeight())
    print("Is this tree BST? ", bst.isBST())
    print("Is this tree balanced? ", bst.isBalanced())