'''
Created on 2015-08-07
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue_in.append(x)

    # @return nothing
    def pop(self):
        if not self.queue_out:
            for elem in reversed(self.queue_in):
                self.queue_out.append(elem)
            del self.queue_in[:]
        self.queue_out.pop(0)

    # @return an integer
    def top(self):
        if self.queue_in:
            return self.queue_in[-1]
        if self.queue_out:
            return self.queue_out[0]
        return None

    # @return an boolean
    def empty(self):
        return (not self.queue_in) and (not self.queue_out)

if __name__ == '__main__':
    pass