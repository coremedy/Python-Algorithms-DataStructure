'''
Created on 2015-07-12

Question: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x

'''

from cc.chap2.node import Node

def partition(head, pivot):
    if head is None:
        return head
    less_than_head = None
    less_than_tail = None
    equal_than_head = None
    equal_than_tail = None
    more_than_head = None
    more_than_tail = None
    while head is not None:
        next_pointer = head.next
        if head.data == pivot:
            if equal_than_head is None:
                equal_than_head = equal_than_tail = head
                equal_than_head.next = None
            else:
                equal_than_tail.next = head
                equal_than_tail = head
                equal_than_tail.next = None
        elif head.data < pivot:
            if less_than_head is None:
                less_than_head = less_than_tail = head
                less_than_head.next = None
            else:
                less_than_tail.next = head
                less_than_tail = head
                less_than_tail.next = None
        else:
            if more_than_head is None:
                more_than_head = more_than_tail = head
                more_than_head.next = None
            else:
                more_than_tail.next = head
                more_than_tail = head
                more_than_tail.next = None
        head = next_pointer
    if (less_than_tail is not None) and (equal_than_head is not None):
        less_than_tail.next = equal_than_head
    if (equal_than_tail is not None) and (more_than_head is not None):
        equal_than_tail.next = more_than_head
    return less_than_head

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 1, 5, 4, 5, 4, 2, 2, 3, 6]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    head_merged = partition(head, 3)
    while head_merged.next is not None:
        print(head_merged.data)
        head_merged = head_merged.next
    print(head_merged.data)