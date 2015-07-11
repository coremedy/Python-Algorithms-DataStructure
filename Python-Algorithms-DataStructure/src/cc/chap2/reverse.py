'''
Created on 2015-07-11

Question: Reverse a linked list, with recursion
'''

from cc.chap2.node import Node

def reverse(head):
    # Baseline
    if head is None:
        return head
    if head.next is None:
        return head
    # Need to back up the next member
    next_member = head.next
    reverse_head = reverse(head.next)
    # After the call, all members from the next one have been reversed
    next_member.next = head
    # Need to set that or the list will not terminate
    head.next = None
    return reverse_head

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 4, 5, 6, 7, 8]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    new_head = reverse(head)
    while new_head.next is not None:
        print(new_head.data)
        new_head = new_head.next
    print(new_head.data)