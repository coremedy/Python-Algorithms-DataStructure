'''
Created on 2014-12-24

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def BinaryTreeList(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    left_node = root.pop(1)
    if len(left_node) > 1:
        root.insert(1, [newBranch, left_node, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    right_node = root.pop(2)
    if len(right_node) > 1:
        root.insert(2, [newBranch, [], right_node])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    r = BinaryTreeList(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    print(getRootVal(r))
    print(getLeftChild(r))
    print(getRightChild(r))
