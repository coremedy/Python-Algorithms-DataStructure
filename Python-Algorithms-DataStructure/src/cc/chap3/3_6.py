'''
Created on 2015-07-15

Question: Write a program to sort a stack in ascending order (with biggest items on top). 
          You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (such as an array).
          The stack supports the following operations: push, pop, peek and isEmpty.
'''

# O(n^2)
def sort_stack(input_stack):
    target_stack = []
    while len(input_stack) > 0:
        elem = input_stack.pop()
        if len(target_stack) == 0:
            target_stack.append(elem)
        else:
            count = 0
            while (len(target_stack) > 0) and (elem < target_stack[-1]):
                input_stack.append(target_stack.pop())
                count += 1
            target_stack.append(elem)
            while count > 0:
                target_stack.append(input_stack.pop())
                count -= 1
    return target_stack

if __name__ == '__main__':
    sample_stack = [1, 10, 111, 9, 2, 8, 0, 7, 5, 6]
    print(sort_stack(sample_stack))