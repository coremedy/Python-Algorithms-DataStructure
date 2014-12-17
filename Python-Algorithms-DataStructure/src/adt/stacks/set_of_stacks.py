'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Stack

'''
We should call it 'list of stacks'
'''
class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        Stack.__init__(self)
        self.setofstacks = []
        self.capacity = capacity
        
    def size(self):
        return (len(self.setofstacks) * self.capacity) + Stack.size(self)
    
    def __repr__(self):
        aux = []
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.items)
        return '{}'.format(aux)
    
    def push(self, value):
        if Stack.size(self) >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = []
        self.items.append(value)
        
    def pop(self):
        val = self.items.pop()
        if (not self.items) and self.setofstacks:
            self.items = self.setofstacks.pop()
        return val

if __name__ == '__main__':
    capacity = 5
    stack = SetOfStacks(capacity)
    print("Is the stack empty? ", stack.isEmpty())
    print("Adding 0 to 10 in the stack...")
    for i in range(10):
        stack.push(i)
    print(stack)
    print("Stack size: ", stack.size())
    print("Stack peek : ", stack.peek())
    print("Pop...", stack.pop())
    print("Stack peek: ", stack.peek())
    print("Is the stack empty? ", stack.isEmpty())
    print(stack)