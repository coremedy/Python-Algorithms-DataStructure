'''
Created on 2015-07-11

'''

class Node(object):
    '''
    classdocs
    '''
    
    def __init__(self, data):
        '''
        Constructor
        '''
        self.data = data
        self.next = None
    
    def append_to_tail(self, data):
        end = Node(data)
        tail = self
        while tail.next is not None:
            tail = tail.next
        tail.next = end