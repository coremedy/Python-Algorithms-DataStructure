'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

class Node(object):
    def __init__(self, value = None, prev_ptr = None, next_ptr = None):
        self.value = value
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr
    
    def getData(self):
        return self.value
    
    def setData(self, new_value):
        self.value = new_value
    
    def getNext(self):
        return self.next_ptr
    
    def setNext(self, new_next_ptr):
        self.next_ptr = new_next_ptr
        
    def getPrev(self):
        return self.prev_ptr
    
    def setPrev(self, new_prev_ptr):
        self.prev_ptr = new_prev_ptr        

if __name__ == '__main__':
    L = Node("a",  None, Node("b",  None, Node("c", None, Node("d"))))
    assert(L.next_ptr.next_ptr.value=='c')
    print(L.getData())
    print(L.getNext().getData())
    L.setData('aa')
    L.setNext(Node('e'))
    print(L.getData())
    print(L.getNext().getData())