'''
Created on 2015-07-11

Question: Write code to remove duplicates from an unsorted linked list.
          How would you solve this problem if a temporary buffer is not allowed?
'''

from cc.chap2.node import Node

def remove_dup(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        val = current.data
        runner_ptr = current
        while runner_ptr.next is not None:
            if runner_ptr.next.data == val:
                runner_ptr.next = runner_ptr.next.next
            else:
                runner_ptr = runner_ptr.next
        if current.next is not None:
            current = current.next
    return head

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 1, 5, 4, 5, 4, 2, 2, 3, 6]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    # Something like selection sort
    head = remove_dup(head)
    data_array.clear()
    while head.next is not None:
        data_array.append(head.data)
        head = head.next
    data_array.append(head.data)
    print(data_array)