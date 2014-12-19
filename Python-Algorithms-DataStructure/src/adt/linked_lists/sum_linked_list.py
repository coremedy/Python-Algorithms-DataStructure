'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

def sumlls(l1, l2):
    
    lsum = LinkedListFIFO()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0
    
    while dig1 and dig2:
        temp_sum = dig1.value + dig2.value + pointer
        if temp_sum > 9:
            pointer = temp_sum // 10
            lsum.addNode(temp_sum % 10)
        else:
            lsum.addNode(temp_sum)
            pointer = 0
        dig1 = dig1.next_ptr
        dig2 = dig2.next_ptr
    
    if dig1:
        while dig1 or pointer:
            temp_sum = pointer
            if dig1:
                temp_sum += dig1.value
            if temp_sum > 9:
                pointer = temp_sum // 10
                lsum.addNode(temp_sum % 10)
            else:
                lsum.addNode(temp_sum)                
                pointer = 0
            if dig1:
                dig1 = dig1.next_ptr
    elif dig2:
        while dig2 or pointer:
            temp_sum = pointer
            if dig2:
                temp_sum += dig2.value
            if temp_sum > 9:
                pointer = temp_sum // 10
                lsum.addNode(temp_sum % 10)
            else:
                lsum.addNode(temp_sum)                
                pointer = 0
            if dig2:
                dig2 = dig2.next_ptr
    elif pointer:
        while pointer:
            temp_sum = pointer
            if temp_sum > 9:
                pointer = temp_sum // 10
                lsum.addNode(temp_sum % 10)
            else:
                lsum.addNode(temp_sum)               
                pointer = 0
                
    return lsum

if __name__ == '__main__':
    l1 = LinkedListFIFO() # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)

    l2 = LinkedListFIFO() # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)

    lsum = sumlls(l1, l2)
    assert(str(lsum) == '<-- [6,2,1,3]')