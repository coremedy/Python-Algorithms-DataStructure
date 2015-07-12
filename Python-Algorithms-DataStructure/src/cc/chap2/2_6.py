'''
Created on 2015-07-12

Question: Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop

'''

from cc.chap2.node import Node

def beginning_of_the_circle(head):
    if head is None:
        return head
    normal_pointer = runner_pointer = head
    # Will meet at (k MOD LEN) steps before the target point
    while (normal_pointer is not None) and (runner_pointer is not None):
        normal_pointer = normal_pointer.next
        runner_pointer = runner_pointer.next
        if runner_pointer is None:
            break
        else:
            runner_pointer = runner_pointer.next
        if runner_pointer is normal_pointer:
            break
    if (normal_pointer is None) or (runner_pointer is None):
        return None
    # Roll back the slow pointer and move both pointers step by step, with k steps
    # We will get the target
    normal_pointer = head
    while True:
        if normal_pointer is runner_pointer:
            break
        else:
            normal_pointer = normal_pointer.next
            runner_pointer = runner_pointer.next
    return normal_pointer

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 1, 5, 4, 5, 4, 2, 2, 3, 6]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    # Generate circular linked list
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head.next.next.next
    print(beginning_of_the_circle(head).data)