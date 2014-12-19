'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

def isPal(l):
    if len(l) < 2:
        return True
    if l[0] != l[-1]:
        return False
    return isPal(l[1:-1])

def checkPal(ll):
    node = ll.head
    l = []
    
    while node:
        l.append(node.value)
        node = node.next_ptr

    return isPal(l)

if __name__ == '__main__':
    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    assert(checkPal(ll) == True)
    ll.addNode(2)
    ll.addNode(3)
    assert(checkPal(ll) == False)