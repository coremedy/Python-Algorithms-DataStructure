'''
Created on 2015-07-12

Question: Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node

'''

from cc.chap2.node import Node

def delete_node(head, node_pointer):
    if (node_pointer is None) or (head is None):
        raise Exception('Input error!') 
    if node_pointer.next is None:
        raise Exception('Not able to process the last one!')
    while node_pointer.next.next is not None:
        node_pointer.data = node_pointer.next.data
        node_pointer = node_pointer.next
    node_pointer.data = node_pointer.next.data
    node_pointer.next = None
    return head

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 1, 5, 4, 5, 4, 2, 2, 3, 6]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    head_modified = delete_node(head, head.next.next.next)
    while head_modified.next is not None:
        print(head_modified.data)
        head_modified = head_modified.next
    print(head_modified.data)