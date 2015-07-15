'''
Created on 2015-07-15

Question: Implement a MyQueue class which implements a queue using two stacks
'''

class MyQueue(object):
    
    def __init__(self):
        self.stack_out = []
        self.stack_in = []
        
    def __shift_stacks(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        
    def peek(self):
        self.__shift_stacks()
        if len(self.stack_out) == 0:
            return None
        else:
            return self.stack_out[-1]
        
    def en_queue(self, data):
        self.stack_in.append(data)
    
    def de_queue(self):
        self.__shift_stacks()
        if len(self.stack_out) == 0:
            return None
        else:
            return self.stack_out.pop()

if __name__ == '__main__':
    q = MyQueue()
    for index in range(1, 8):
        q.en_queue(index)
    print(q.de_queue())
    print(q.de_queue())
    print(q.de_queue())
    for index in range(8, 16):
        q.en_queue(index)
    value = q.de_queue()
    while value is not None:
        print(value)
        value = q.de_queue()