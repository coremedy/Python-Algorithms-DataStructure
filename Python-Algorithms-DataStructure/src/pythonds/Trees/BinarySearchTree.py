'''
Created on 2014-12-26
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
                currentNode.leftChild = TreeNode(key, val, parent = currentNode, depth = currentNode.depth + 1)
                self.size = self.size + 1
        else:
            if currentNode.hasRightChild():
                self.__put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode, depth = currentNode.depth + 1)
                self.size = self.size + 1
    
    def put(self,key,val):
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
    
    def get(self,key):
        if self.root:
            res = self.__get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
            
    # use this data structure like dict
    def __setitem__(self, k, v):
        self.put(k,v)

    # use this data structure like dict
    def __getitem__(self, key):
        return self.get(key)
    
    # in
    def __contains__(self, key):
        if self.__get(key, self.root):
            return True
        else:
            return False
    
    # del
    def __delitem__(self,key):
        self.delete(key)
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.__get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        # the root node is a leaf
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
        
    def remove(self, currentNode):
        # leaf, and the size of tree is greater than 1
        if currentNode.isLeaf():
            if currentNode is currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # the target node has two children
        # we will be able to find a successor
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # the target node has only left child
        elif currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.leftChild
                currentNode.leftChild.adjustDepth(currentNode.depth)
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.leftChild
                currentNode.leftChild.adjustDepth(currentNode.depth)
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
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
                currentNode.rightChild.adjustDepth(currentNode.depth)
            else:
                currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
                if currentNode.leftChild:
                    currentNode.leftChild.adjustDepth(currentNode.depth - 1)
                if currentNode.rightChild:
                    currentNode.rightChild.adjustDepth(currentNode.depth - 1)

if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree.delete(3)