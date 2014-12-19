'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

# This works well for single-linked list
# For double-linked list, it will be simpler
class LinkedListFIFO_find_kth(LinkedListFIFO):
    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k:
                p2 = p2.next_ptr
            p1 = p1.next_ptr
            i += 1
        return p2
    
if __name__ == '__main__':
    ll = LinkedListFIFO_find_kth()
    for i in range(1, 11):
        ll.addNode(i)
    print('The Linked List:' + str(ll))
    k = 3
    k_from_last = ll.find_kth_to_last(k)
    print("The %dth element to the last of the LL of size %d is %d" % (k, ll.length, k_from_last.getData()))