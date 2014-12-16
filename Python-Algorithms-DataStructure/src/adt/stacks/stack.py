'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return not bool(self.items)
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self.items[-1]
    
    def __repr__(self, *args, **kwargs):
        return '{}'.format(self.items)
    

class Node(object):
    def __init__(self, value, left_ptr = None, right_ptr = None):
        self.val = value
        self.left_pointer = left_ptr
        self.right_pointer = right_ptr
        
class Linked_Stack(object):
    def __init__(self):
        self.top_ptr = None
        self.sz = 0
    
    def isEmpty(self):
        return not bool(self.top_ptr)
    
    def push(self, item):
        if self.top_ptr is None:
            self.top_ptr = Node(item)
        else:
            node = Node(item, None, self.top_ptr)
            self.top_ptr.left_pointer = node
            self.top_ptr = node
        self.sz += 1
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            node = self.top_ptr
            self.top_ptr = node.right_pointer
            self.top_ptr.left_pointer = None
            self.sz -= 1
            return node.val
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            return self.top_ptr.val
        
    def size(self):
        return self.sz
    
    def __repr__(self, *args, **kwargs):
        rep = '['
        current = self.top_ptr
        while current is not None:
            rep += '{}'.format(current.val)
            current = current.right_pointer
            if current is not None:
                rep += ','        
        rep += ']'    
        return rep

if __name__ == '__main__':
    stack = Linked_Stack()
    print("Is the stack empty? ", stack.isEmpty())
    print("Adding 0 to 10 in the stack...")
    for i in range(10):
        print(i)
        stack.push(i)
    print("Stack size: ", stack.size())
    print("Stack peek : ", stack.peek())
    print("Pop...", stack.pop())
    print("Stack peek: ", stack.peek())
    print("Is the stack empty? ", stack.isEmpty())
    print(stack)