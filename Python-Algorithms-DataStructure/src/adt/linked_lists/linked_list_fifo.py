'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.node import Node

class LinkedListFIFO(object):
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
        
    def __repr__(self, *args, **kwargs):
        rep = '<-- ['
        current = self.head
        while current:
            rep += '{}'.format(current.value)
            current = current.next_ptr
            if current:
                rep += ','        
        rep += ']'    
        return rep
    
    def __add_first(self, value):
        self.head = self.tail = Node(value)
        self.length = 1
        
    def __add(self, value):
        self.tail.next_ptr = Node(value, self.tail, None)
        self.tail = self.tail.next_ptr
        self.length += 1
    
    def addNode(self, value):
        if not self.head:
            self.__add_first(value)
        else:
            self.__add(value)
            
    def __find_with_index(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next_ptr
            i += 1
        return node, prev, i
        
    def __delete_first(self):
        self.head = self.tail = None
        self.length = 0
        print('The list is empty.')
    
    def delete_node_with_index(self, index):
        if (not self.head) or (not self.head.next_ptr):
            self.__delete_first()
        else:
            node, prev, i = self.__find_with_index(index)
            if (i == index) and node:
                if (i == 0) or (not prev):
                    self.head = node.next_ptr
                    self.head.prev_ptr = None
                elif node is self.tail:
                    self.tail = prev
                    self.tail.next_ptr = None
                else:
                    prev.next_ptr = node.next_ptr
                    node.next_ptr.prev_ptr = prev
                self.length -= 1
            else:
                print('Node with index {} not found'.format(index))

if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.addNode(i)
    print('The list is:' + str(ll))
    ll.delete_node_with_index(2)
    print('The list after deleting node with index 2:' + str(ll))
    ll.addNode(15)
    print('The list after adding node with value 15:' + str(ll))
    for i in range(ll.length-1, -1, -1):
        ll.delete_node_with_index(i)
    print("The list after deleting everything...:" + str(ll))