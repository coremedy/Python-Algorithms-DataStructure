'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

def isCircularll(ll):
    ptr1 = ll.head
    ptr2 = ll.head
    
    # use ptr2 here since it will terminate faster than ptr1 in case the linked list is not circular
    while ptr2:
        try:
            ptr1 = ptr1.next_ptr
            ptr2 = ptr2.next_ptr.next_ptr
        except:
            break
        
        if ptr1 is ptr2:
            return True
        
    return False

if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(10):
        ll.addNode(i)
    print(isCircularll(ll))
    # Do something evil ...
    ll.tail.next_ptr = ll.head
    ll.head.prev_ptr = ll.tail
    print(isCircularll(ll))