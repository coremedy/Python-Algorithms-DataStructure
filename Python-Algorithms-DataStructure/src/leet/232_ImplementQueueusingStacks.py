'''
Created on 2015-08-07
Dirty implementation
'''

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop(0)

    # @return an integer
    def peek(self):
        if self.stack:
            return self.stack[0]
        else:
            return None

    # @return an boolean
    def empty(self):
        if self.stack:
            return False
        else:
            return True

if __name__ == '__main__':
    pass