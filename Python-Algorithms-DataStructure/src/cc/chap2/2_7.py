'''
Created on 2015-07-12

Question: Implement a function to check if a linked list is a palindrome
'''

from cc.chap2.node import Node

def length_of_linked_list(head):
    length = 0
    if head is None:
        return length
    while head is not None:
        length += 1
        head = head.next
    return length

def is_palindrome_worker(head, length, result):
    # Baseline
    if length == 1:
        return head.next
    elif length == 2:
        if head.data != head.next.data:
            result[0] = False
        return head.next.next
    else:
        # Real work
        node_to_compare = is_palindrome_worker(head.next, length - 2, result)
        if head.data != node_to_compare.data:
            result[0] = False
        return node_to_compare.next

# We can also use runner pointer here for iterative version, one 1x speed, one 2x speed, and the list will be divided by half
def is_palindrome_recursive(head):
    length = length_of_linked_list(head)
    if (length == 0) or (length == 1):
        return True
    result = [True]
    is_palindrome_worker(head, length, result)
    return result[0]

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 5, 4, 11, 4, 5, 2, 1]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    print(is_palindrome_recursive(head))