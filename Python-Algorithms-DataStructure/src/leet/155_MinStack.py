'''
Created on 2015-08-07
'''

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.stack_min = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.stack_min.append(x)
        else:
            self.stack.append(x)
            self.stack_min.append(self.stack_min[-1] if self.stack_min[-1] < x else x)

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    # @return an integer
    def getMin(self):
        if self.stack_min:
            return self.stack_min[-1]
        return None

if __name__ == '__main__':
    pass