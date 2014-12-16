'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Node

class Queue(object):
    
    def __init__(self):
        self.item = []
        
    def isEmpty(self):
        return not bool(self.item)
    
    def enqueue(self, value):
        self.item.append(value)
        
    '''
    O(n)
    '''
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.item.pop(0)
        
    def size(self):
        return len(self.item)
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.item[0]
    
    def __repr__(self, *args, **kwargs):
        return "<-- {} <--".format(self.item)
    
class Linked_Queue(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0
    
    def isEmpty(self):
        return not bool(self.head)
    
    def enqueue(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None, None)
        else:
            node = Node(value, self.tail, None)
            self.tail.right_pointer = node
            self.tail = node
        self.sz += 1
    
    def size(self):
        return self.sz
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.head.val
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            val = self.head.val
            self.head = self.head.right_pointer
            if self.head is None:
                self.tail = None
            else:
                self.head.left_pointer = None
            return val

    def __repr__(self, *args, **kwargs):
        rep = '<-- ['
        current = self.head
        while current is not None:
            rep += '{}'.format(current.val)
            current = current.right_pointer
            if current is not None:
                rep += ','        
        rep += '] <---'    
        return rep

if __name__ == '__main__':
    queue = Linked_Queue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 0 to 9 in the queue...")
    for i in range(10):
        queue.enqueue(i)
    print("Queue size: ", queue.size())
    print("Queue peek : ", queue.peek())
    print("Dequeue...", queue.dequeue())
    print("Queue peek: ", queue.peek())
    print("Is the queue empty? ", queue.isEmpty())
    print(queue)