'''
Created on 2015-07-15

Question: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
          Therefore, in real life, we would like start a new stack when the previous stack exceeds some threshold.
          Implement a data structure SetOfStacks that mimics this.
          SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
          SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack(that is, pop() should return the same value as it would if there were just a single stack).

          FOLLOW UP
          Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''

class SetOfStacks(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.set_of_stacks = []
        self.last_stack = -1
        
    def push(self, data):
        if self.last_stack == -1:
            self.set_of_stacks.append([data])
            self.last_stack = 0
        else:
            if len(self.set_of_stacks[self.last_stack]) < self.capacity:
                self.set_of_stacks[self.last_stack].append(data)
            else:
                self.set_of_stacks.append([data])
                self.last_stack += 1
    
    def pop(self):
        if self.last_stack == -1:
            return None
        else:
            if len(self.set_of_stacks[self.last_stack]) > 0:
                val = self.set_of_stacks[self.last_stack].pop()
                if len(self.set_of_stacks[self.last_stack]) == 0:
                    self.set_of_stacks.pop()
                    self.last_stack -= 1                    
                return val                 

    def popAt(self, index):
        if (self.last_stack == -1) or (index < 0):
            return None
        elif index > self.last_stack:
            return None
        else:
            if index == self.last_stack:
                return self.pop()
            else:
                val = self.set_of_stacks[index].pop()
                while True:
                    self.set_of_stacks[index].append(self.set_of_stacks[index + 1].pop(0))
                    index += 1
                    if index == self.last_stack:
                        if len(self.set_of_stacks[self.last_stack]) == 0:
                            self.set_of_stacks.pop()
                            self.last_stack -= 1                        
                        break
                return val
       
if __name__ == '__main__':
    s = SetOfStacks(4)
    for index in range(0, 13):
        s.push(index)
    print(s.set_of_stacks)
    s.popAt(2)
    print(s.set_of_stacks)
    s.popAt(1)
    print(s.set_of_stacks)
    for index in range(0, 11):
        s.pop()
        print(s.set_of_stacks)