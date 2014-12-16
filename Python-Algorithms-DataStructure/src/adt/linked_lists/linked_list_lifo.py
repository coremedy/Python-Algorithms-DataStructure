'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.node import Node

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __repr__(self, *args, **kwargs):
        rep = '['
        current = self.head
        while current:
            rep += '{}'.format(current.value)
            current = current.next_ptr
            if current:
                rep += ','        
        rep += '] --->'    
        return rep
    
    def _delete(self, prev, node):
        if not prev:
            self.head = node.next_ptr
            if self.head:
                self.head.prev_ptr = None
        else:
            if self.tail is node:
                prev.next_ptr = None
                self.tail = prev
            else:
                node.prev_ptr.next_ptr = node.next_ptr
                node.next_ptr.prev_ptr = node.prev_ptr
        self.length -= 1
    
    def _add(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            self.tail.next_ptr = Node(value, self.tail)
            self.tail = self.tail.next_ptr
        self.length += 1
    
    def _find_by_index(self, index):
        prev = None
        curr = self.head
        i = 0
        while curr and i < index:
            prev = curr
            curr = curr.next_ptr
            i += 1
        return curr, prev, i
    
    def _find_by_value(self, value):
        prev = None
        curr = self.head
        found = False
        while curr and not found:
            if curr.value == value:
                found = True
            else:
                prev = curr
                curr = curr.next_ptr
        return curr, prev, found
    
    def _delete_node_by_index(self, index):
        curr, prev, i = self._find_by_index(index)
        if index == i:
            self._delete(prev, curr)
        else:
            print('Node with index {} not found'.format(index))
    
    def _delete_node_by_value(self, value):
        curr, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, curr)
        else:
            print('Node with value {} not found'.format(value))   

if __name__ == '__main__':
    ll = LinkedListLIFO()
    for i in range(1, 5):
        ll._add(i)
    print('The list is:' + str(ll))
    ll._delete_node_by_index(2)
    print('The list after deleting node with index 2:' + str(ll))
    ll._delete_node_by_value(2)
    print('The list after deleting node with value 3:' + str(ll))
    ll._add(15)
    print('The list after adding node with value 15:' + str(ll))
    for i in range(ll.length-1, -1, -1):
        ll._delete_node_by_index(i)
    print('The list after deleting everything...' + str(ll))