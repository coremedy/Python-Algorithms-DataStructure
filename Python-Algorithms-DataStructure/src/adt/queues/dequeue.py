'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Node

class Deque(object):
    
    def __init__(self):
        self.left_pointer = None
        self.right_pointer = None
        self.sz = 0
    
    def isEmpty(self):
        return not bool(self.left_pointer)
    
    def size(self):
        return self.sz
    
    def enqueue_left(self, value):
        if self.isEmpty():
            self.left_pointer = self.right_pointer = Node(value)
        else:
            node = Node(value, None, self.left_pointer)
            self.left_pointer.left_pointer = node
            self.left_pointer = node

    def enqueue_right(self, value):
        if self.isEmpty():
            self.left_pointer = self.right_pointer = Node(value)
        else:
            node = Node(value, self.right_pointer, None)
            self.right_pointer.right_pointer = node
            self.right_pointer = node

    def dequeue_left(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            node = self.left_pointer
            self.left_pointer = self.left_pointer.right_pointer
            if self.left_pointer is None:
                self.right_pointer = None
            else:
                self.left_pointer.left_pointer = None
            return node.val
    
    def dequeue_right(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            node = self.right_pointer
            self.right_pointer = self.right_pointer.left_pointer
            if self.right_pointer is None:
                self.left_pointer = None
            else:
                self.right_pointer.right_pointer = None
            return node.val

    def peek_left(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.left_pointer.val
    
    def peek_right(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.right_pointer.val
    
    def __repr__(self, *args, **kwargs):
        rep = '<-- ['
        current = self.left_pointer
        while current is not None:
            rep += '{}'.format(current.val)
            current = current.right_pointer
            if current is not None:
                rep += ','        
        rep += '] --->'    
        return rep

if __name__ == '__main__':
    queue = Deque()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 0 to 9 in the queue...")
    for i in range(10):
        if i % 2 == 0 :
            queue.enqueue_right(i)
        else:
            queue.enqueue_left(i)
    print(queue)
    print("Queue size: ", queue.size())
    print("Queue peek left: ", queue.peek_left())
    print("Dequeue left ...", queue.dequeue_left())
    print("Queue peek left: ", queue.peek_left())
    print("Queue peek right: ", queue.peek_right())
    print("Dequeue right ...", queue.dequeue_right())
    print("Queue peek right: ", queue.peek_right())
    print("Is the queue empty? ", queue.isEmpty())
    print(queue)
    '''
    We also have a built-in dequeue container
    from collections import dequeue
    '''