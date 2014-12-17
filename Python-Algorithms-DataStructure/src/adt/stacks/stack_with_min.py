'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        self.minimum = minimum
        
class StackMin(object):
    def __init__(self):
        self.items = []
        self.minimum = int(0x07fffffff)
        
    def isEmpty(self):
        return not self.items

    def push(self, value):
        if not self.items or self.minimum > value:
            self.minimum = value
        self.items.append(NodeWithMin(value, self.minimum))
        
    def peek(self):
        return self.items[-1].value
    
    def peekMinimum(self):
        return self.items[-1].minimum
    
    def pop(self):
        item = self.items.pop()
        if item:
            if item.value == self.minimum:
                self.minimum = self.peekMinimum()
            return item.value
        else:
            print("Stack is empty.")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return '{}'.format(aux)

if __name__ == '__main__':
    stack = StackMin()
    print("Is the stack empty? ", stack.isEmpty())
    print("Adding 0 to 10 in the stack...")
    for i in range(10, -1, -1):
        stack.push(i)
    for i in range(1, 5):
        stack.push(i)
    print(stack)
    print("Stack size: ", len(stack.items))
    print("Stack peek and peekMinimum : ", stack.peek(),
    stack.peekMinimum())
    print("Pop...", stack.pop())
    print("Stack peek and peekMinimum : ", stack.peek(),
    stack.peekMinimum())
    print("Is the stack empty? ", stack.isEmpty())
    print(stack)