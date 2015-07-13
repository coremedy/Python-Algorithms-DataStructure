'''
Created on 2015-07-13

Question: How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
          Push, pop and min should all operate in O(1) time.
'''

class StackWithMin(object):
    
    def __init__(self):
        self.data_array = []
        self.minimal_array = []
        
    def push(self, value):
        self.data_array.append(value)
        if len(self.minimal_array) == 0:
            self.minimal_array.append(value)
        else:
            # Use <= here!
            if value <= self.minimal_array[-1]:
                self.minimal_array.append(value)
    
    def pop(self):
        if len(self.data_array) == 0:
            return None
        else:
            top_value = self.data_array.pop()
            if top_value == self.minimal_array[-1]:
                self.minimal_array.pop()
            return top_value
    
    def min(self):
        if len(self.minimal_array) == 0:
            return None
        else:
            return self.minimal_array[-1]      
        
if __name__ == '__main__':
    stack_with_min = StackWithMin()
    for elem in [10, 9, 8, 7, 9, 7, 6, 3, 5, 4, 3, 2, 1]:
        stack_with_min.push(elem)
    while True:
        top_value = stack_with_min.pop()
        if top_value is None:
            break
        else:
            print(stack_with_min.min())