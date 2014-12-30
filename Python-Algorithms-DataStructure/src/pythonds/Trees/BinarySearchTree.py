'''
Created on 2014-12-30
Code coming from: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
'''

from pythonds.Trees.TreeNode import TreeNode

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def __put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.__put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode, depth=currentNode.depth + 1)
                self.updateBalance_AddNode(currentNode.leftChild)
                self.size = self.size + 1
        else:
            if currentNode.hasRightChild():
                self.__put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode, depth=currentNode.depth + 1)
                self.updateBalance_AddNode(currentNode.rightChild)
                self.size = self.size + 1
    
    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size = self.size + 1
            
    def __get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self.__get(key, currentNode.leftChild)
        else:
            return self.__get(key, currentNode.rightChild)            
    
    def get(self, key):
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
            
    # use this data structure like dict
    def __setitem__(self, k, v):
        self.put(k, v)

    # use this data structure like dict
    def __getitem__(self, key):
        return self.get(key)
    
    # in
    def __contains__(self, key):
        if self.__get(key, self.root):
            return True
        else:
            return False
    
    def __findMin(self, node):
        current = node
        if current:
            while current.hasLeftChild():
                current = current.leftChild
        return current
    
    def __findSuccessor(self, node):
        succ = None
        if node:
            if node.rightChild:
                succ = self.__findMin(node.rightChild)
            else:
                if node.parent:
                    if node.isLeftChild():
                        succ = node.parent
                    else:
                        node.parent.rightChild = None
                        succ = self.__findSuccessor(node.parent)
                        node.parent.rightChild = node
        return succ
    
    def __spliceOut(self, node):
        if node:
            if node.isLeaf():
                if node.isLeftChild():
                    node.parent.leftChild = None
                    self.updateBalance_DelNode(node.parent)
                else:
                    node.parent.rightChild = None
                    self.updateBalance_DelNode(node.parent, left = False)
            elif node.hasAnyChildren():
                if node.hasLeftChild():
                    if node.isLeftChild():
                        node.parent.leftChild = node.leftChild
                        node.leftChild.parent = node.parent
                        node.leftChild.adjustDepth(node.depth)
                        self.updateBalance_DelNode(node.parent)
                    else:
                        node.parent.rightChild = node.leftChild
                        node.leftChild.parent = node.parent
                        node.leftChild.adjustDepth(node.depth)
                        self.updateBalance_DelNode(node.parent, left = False)
                else:
                    if node.isLeftChild():
                        node.parent.leftChild = node.rightChild
                        node.rightChild.parent = node.parent
                        node.rightChild.adjustDepth(node.depth)                          
                        self.updateBalance_DelNode(node.parent)
                    else:
                        node.parent.rightChild = node.rightChild
                        node.rightChild.parent = node.parent
                        node.rightChild.adjustDepth(node.depth)
                        self.updateBalance_DelNode(node.parent, left = False)

    # del
    def __delitem__(self, key):
        self.delete(key)
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.__get(key, self.root)
            if nodeToRemove:
                self.__remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        # the root node is a leaf
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
        
    def __remove(self, currentNode):
        # leaf, and the size of tree is greater than 1
        if currentNode.isLeaf():
            if currentNode is currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
                self.updateBalance_DelNode(currentNode.parent)
            else:
                currentNode.parent.rightChild = None
                self.updateBalance_DelNode(currentNode.parent, left = False)
        # the target node has two children
        # we will be able to find a successor
        elif currentNode.hasBothChildren():
            succ = self.__findSuccessor(currentNode)
            self.__spliceOut(succ)
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # the target node has only left child
        elif currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChild
                currentNode.leftChild.adjustDepth(currentNode.depth)
                self.updateBalance_DelNode(currentNode.parent)
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.leftChild
                currentNode.leftChild.adjustDepth(currentNode.depth)
                self.updateBalance_DelNode(currentNode.parent, left = False)
            # root node
            else:
                currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
                if currentNode.leftChild:
                    currentNode.leftChild.adjustDepth(currentNode.depth - 1)
                if currentNode.rightChild:
                    currentNode.rightChild.adjustDepth(currentNode.depth - 1)
        # the target node has only right child
        else:
            if currentNode.isLeftChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.rightChild
                currentNode.rightChild.adjustDepth(currentNode.depth)
                self.updateBalance_DelNode(currentNode.parent)
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
                currentNode.rightChild.adjustDepth(currentNode.depth)
                self.updateBalance_DelNode(currentNode.parent, left = False)
            else:
                currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
                if currentNode.leftChild:
                    currentNode.leftChild.adjustDepth(currentNode.depth - 1)
                if currentNode.rightChild:
                    currentNode.rightChild.adjustDepth(currentNode.depth - 1)                   
                    
    # This should happen between a node and its right child
    def rotateLeft(self, rotationRoot):
        newRoot = rotationRoot.rightChild
        oldDepth = rotationRoot.depth
        # update children first
        rotationRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild:
            newRoot.leftChild.parent = rotationRoot
        # update parent
        newRoot.parent = rotationRoot.parent
        if rotationRoot.isRoot():
            self.root = newRoot
        elif rotationRoot.isLeftChild():
            rotationRoot.parent.leftChild = newRoot
        else:
            rotationRoot.parent.rightChild = newRoot
        # update relationship
        newRoot.depth, rotationRoot.depth = rotationRoot.depth, newRoot.depth
        newRoot.leftChild = rotationRoot
        rotationRoot.parent = newRoot
        # update balance factor
        rotationRoot.balanceFactor = rotationRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotationRoot.balanceFactor, 0)
        # update depth
        newRoot.adjustDepth(oldDepth)
    
    # This should happen between a node and its left child
    def rotateRight(self, rotationRoot):
        newRoot = rotationRoot.leftChild
        oldDepth = rotationRoot.depth
        # update children first
        rotationRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild:
            newRoot.rightChild.parent = rotationRoot
        # update parent
        newRoot.parent = rotationRoot.parent
        if rotationRoot.isRoot():
            self.root = newRoot
        elif rotationRoot.isLeftChild():
            rotationRoot.parent.leftChild = newRoot
        else:
            rotationRoot.parent.rightChild = newRoot
        # update relationship
        newRoot.rightChild = rotationRoot
        rotationRoot.parent = newRoot
        # update balance factor
        rotationRoot.balanceFactor = rotationRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + max(rotationRoot.balanceFactor, 0)
        # update depth
        newRoot.adjustDepth(oldDepth)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        else:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
            self.rotateRight(node)
            
    def updateBalance_AddNode(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            else:
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance_AddNode(node.parent)
                
    def updateBalance_DelNode(self, node, left = True):
        if left:
            node.balanceFactor -= 1
        else:
            node.balanceFactor += 1
        if node.balanceFactor:
            if node.balanceFactor < -1 or node.balanceFactor > 1:
                self.rebalance(node)
            else:
                if not node.isRoot():
                    if node.isLeftChild():
                        self.updateBalance_DelNode(node.parent)
                    else:
                        self.updateBalance_DelNode(node.parent, left = False)

if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[1] = "hi"
    mytree[2] = "at"
    mytree[3] = "red"
    mytree[5] = "blue"
    mytree[6] = "yellow"
    mytree[4] = "naughty"
    mytree.delete(3)