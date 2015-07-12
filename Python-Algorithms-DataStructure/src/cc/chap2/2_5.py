'''
Created on 2015-07-12

Question: You have two numbers represented by a linked list, where each node contains a single digit.
          The digits are stored in reverse order, such that the 1's digit is at the head of the list.
          Write a function that adds the two numbers and returns the sum as a linked list.
          Case 1:
          (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
          Case 2: Suppose the digits are stored in forward order. Repeat the above problem.
          (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 716 + 592.
'''

from cc.chap2.node import Node

# Case 1
def addition_recursive_case1_worker(head_left, head_right, carry):
    # Baseline
    if (head_left is None) and (head_right is None):
        if carry != 0:
            return Node(carry)
        else:
            return None
    # Start from the lowest digit
    new_value = 0
    if head_left is not None:
        new_value += head_left.data
        head_left = head_left.next
    if head_right is not None:
        new_value += head_right.data
        head_right = head_right.next
    new_value += carry
    new_node = Node(new_value % 10)
    new_node.next = addition_recursive_case1_worker(head_left, head_right, new_value // 10)
    return new_node    

def addition_recursive_case1(head_left, head_right):
    if (head_left is None) and (head_right is None):
        return None
    elif (head_left is not None) and (head_right is not None):
        return addition_recursive_case1_worker(head_left, head_right, 0)
    elif (head_left is None) and (head_right is not None):
        return head_right
    else:
        return head_left
    
# Case 2
def length_of_linked_list(head):
    length = 0
    if head is None:
        return length
    while head is not None:
        length += 1
        head = head.next
    return length

def pad_linked_list(head, gap):
    for index in range(0, gap):
        tmp_node = Node(0)
        tmp_node.next = head
        head = tmp_node
    return head
 
def addition_recursive_case2_worker(head_left, head_right, carry):
    # Baseline - no need to check carry
    if (head_left is None) and (head_right is None):
        return None
    lower_digit_pointer = addition_recursive_case2_worker(head_left.next, head_right.next, carry)
    new_value = carry[0]
    new_value += head_left.data
    new_value += head_right.data
    carry[0] = new_value // 10
    new_node = Node(new_value % 10)
    new_node.next = lower_digit_pointer
    return new_node
    
def addition_recursive_case2(head_left, head_right):
    if (head_left is None) and (head_right is None):
        return None
    elif (head_left is not None) and (head_right is not None):
        length_left = length_of_linked_list(head_left)
        length_right = length_of_linked_list(head_right)
        if length_left > length_right:
            head_right = pad_linked_list(head_right, length_left - length_right)
        elif length_right > length_left:
            head_left = pad_linked_list(head_left, length_right - length_left)
            carry = [0]
            new_head = addition_recursive_case2_worker(head_left, head_right, carry)
            # One more step here
            if carry[0] != 0:
                new_head_carry = Node(carry[0])
                new_head_carry.next = new_head
                return new_head_carry
            else:
                return new_head
    elif (head_left is None) and (head_right is not None):
        return head_right
    else:
        return head_left

if __name__ == '__main__':
    # Case 1: generate a sample linked list
    data_array = [7, 1, 6] # 617
    head_left = Node(data_array[0])
    for index in range(1, len(data_array)):
        head_left.append_to_tail(data_array[index])
    data_array = [5, 9, 3, 9] # 9395
    head_right = Node(data_array[0])
    for index in range(1, len(data_array)):
        head_right.append_to_tail(data_array[index])
    head_result = addition_recursive_case1(head_left, head_right)
    while head_result.next is not None:
        print(head_result.data)
        head_result = head_result.next
    print(head_result.data)
    # Case 2: generate a sample linked list
    data_array = [6, 1, 7] # 617
    head_left = Node(data_array[0])
    for index in range(1, len(data_array)):
        head_left.append_to_tail(data_array[index])
    data_array = [9, 3, 9, 5] # 9395
    head_right = Node(data_array[0])
    for index in range(1, len(data_array)):
        head_right.append_to_tail(data_array[index])
    head_result = addition_recursive_case2(head_left, head_right)
    while head_result.next is not None:
        print(head_result.data)
        head_result = head_result.next
    print(head_result.data)