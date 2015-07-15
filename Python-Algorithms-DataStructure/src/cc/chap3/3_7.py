'''
Created on 2015-07-15

Question: An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
          People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
          They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDong and dequeueCat.
          You may use the built-in LinkedList data structure. 
'''

from cc.chap2.node import Node

class Animal(object):
    
    def __init__(self, nick_name):
        self.nick_name = nick_name
        
    def get_nick_name(self):
        return self.nick_name
    
    def set_arrival_order(self, order):
        self.arrival_order = order
        
    def get_arrival_order(self):
        return self.arrival_order
    
    def come_first_than(self, a):
        return self.arrival_order < a.get_arrival_order()
    
class Cat(Animal):
    
    def __init__(self, nick_name):
        super().__init__(nick_name)

class Dog(Animal):
    
    def __init__(self, nick_name):
        super().__init__(nick_name)
        
class AnimalShelter(object):
    
    def __init__(self):
        self.dog_queue_head = None
        self.dog_queue_tail = None
        self.cat_queue_head = None
        self.cat_queue_tail = None
        self.order = 0
        
    def cat_dequeue(self):
        if self.cat_queue_head is None:
            return None
        else:
            a = self.cat_queue_head.data
            self.cat_queue_head = self.cat_queue_head.next
            if self.cat_queue_head is None:
                self.cat_queue_tail = None
            return a
    
    def dog_dequeue(self):
        if self.dog_queue_head is None:
            return None
        else:
            a = self.dog_queue_head.data
            self.dog_queue_head = self.dog_queue_head.next
            if self.dog_queue_head is None:
                self.dog_queue_tail = None
            return a
     
    def animal_enqueue(self, a):
        a.set_arrival_order(self.order)
        self.order += 1
        if isinstance(a, Dog):
            if self.dog_queue_head is None:
                self.dog_queue_head = self.dog_queue_tail = Node(a)
            else:
                self.dog_queue_tail.next = Node(a)
                self.dog_queue_tail = self.dog_queue_tail.next
        else:
            if self.cat_queue_head is None:
                self.cat_queue_head = self.cat_queue_tail = Node(a)
            else:
                self.cat_queue_tail.next = Node(a)
                self.cat_queue_tail = self.cat_queue_tail.next
    
    def any_dequeue(self):
        if (self.dog_queue_head is None) and (self.cat_queue_head is None):
            return None
        elif (self.dog_queue_head is not None) and (self.cat_queue_head is not None):
            if self.dog_queue_head.data.come_first_than(self.cat_queue_head.data):
                return self.dog_dequeue()
            else:
                return self.cat_dequeue()
        elif (self.dog_queue_head is not None) and (self.cat_queue_head is None):
            return self.dog_dequeue()
        else:
            return self.cat_dequeue()

if __name__ == '__main__':
    a = AnimalShelter()
    a.animal_enqueue(Cat('Miu~1'))
    a.animal_enqueue(Cat('Miu~2'))
    a.animal_enqueue(Dog('Woo~1'))    
    a.animal_enqueue(Dog('Woo~2'))
    a.animal_enqueue(Dog('Woo~3'))
    a.animal_enqueue(Cat('Miu~3'))
    print(a.any_dequeue().get_nick_name())
    print(a.cat_dequeue().get_nick_name())
    print(a.any_dequeue().get_nick_name())
    print(a.dog_dequeue().get_nick_name())
    print(a.dog_dequeue().get_nick_name())    
    print(a.any_dequeue().get_nick_name())