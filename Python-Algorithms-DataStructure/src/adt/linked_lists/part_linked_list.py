'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()
    
    node = ll.head
    while node:
        item = node.value
        
        if item < n:
            less.addNode(item)
        elif item > n:
            more.addNode(item)
            
        node = node.next_ptr
    
    less.addNode(n)
    
    node = more.head
    while node:
        less.addNode(node.value)
        node = node.next_ptr
    
    return less

if __name__ == '__main__':
    ll = LinkedListFIFO()
    l = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l:
        ll.addNode(i)
    print('Before Part: ', str(ll))
    print('After Part: ', str(partList(ll, 6)))