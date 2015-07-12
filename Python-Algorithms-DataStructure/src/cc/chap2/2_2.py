'''
Created on 2015-07-12

Question: Implement an algorithm to find the kth to last element of a singly linked list

'''

from cc.chap2.node import Node

def find_kth_iterative(head, k):
    # Need to use the runner pointer
    start_pointer = runner_pointer = head
    for index in range(1, k):
        # Exceed the limit
        if runner_pointer is None:
            return runner_pointer
        else:
            runner_pointer = runner_pointer.next
    # Run, run, run!
    while True:
        if runner_pointer.next is None:
            break
        start_pointer = start_pointer.next
        runner_pointer = runner_pointer.next
    return start_pointer

def find_kth_recursive_worker(head, k, recorder):
    # Baseline
    if head is None:
        return head
    # Go to bottom first
    last_return = find_kth_recursive_worker(head.next, k, recorder)
    # Calc the level
    recorder[0] += 1
    # Hit
    if recorder[0] == k:
        return head
    # Not hit
    return last_return

def find_kth_recursive(head, k):
    return find_kth_recursive_worker(head, k, [0])

if __name__ == '__main__':
    # Generate a sample linked list
    data_array = [1, 2, 3, 1, 5, 4, 5, 4, 2, 2, 3, 6]
    head = Node(data_array[0])
    for index in range(1, len(data_array)):
        head.append_to_tail(data_array[index])
    print(find_kth_recursive(head, 5).data)
    print(find_kth_iterative(head, 9).data)