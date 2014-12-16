'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.linked_lists.linked_list_fifo import LinkedListFIFO

class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self.__create_hash_table()
        
    def __create_hash_table(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())
    
    def __find(self, item):
        return item % self.size
    
    def add(self, item):
        self.slots[self.__find(item)].addNode(item)

    def delete(self, item):
        # not so good here, need to change to delete_node_with_value
        self.slots[self.__find(item)].delete_node_with_index(item)
        
    def _print(self):
        for i in range(self.size):
            print('\nSlot {}:'.format(i))
            print(str(self.slots[i]))

if __name__ == '__main__':
    H1 = HashTableLL(3)
    for i in range (0, 20):
        H1.add(i)
    H1._print()
    print('\n\nNow deleting:')
    H1.delete(0)
    H1.delete(1)
    H1.delete(2)
    H1.delete(0)
    H1._print()