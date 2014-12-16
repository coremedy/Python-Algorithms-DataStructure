'''
Created on 2014-12-16

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

'''
A really good example to understand the beauty of Python
http://www.diveintopython.net/power_of_introspection/and_or.html
'''
class Heapify(object):
    def __init__(self, data = None):
        # If data is not None, self.data = data
        # If data is None, self.data = []
        self.data = data or []
        # Start from the parents of the leaf node, understand?
        for i in range(len(self.data) // 2, -1, -1):
            self.__max_heapify__(i)
        
    def __repr__(self, *args, **kwargs):
        return '{}'.format(self.data)
    
    def __parent(self, i):
        return i >> 1
    
    def __left_child(self, i):
        return (i << 1) + 1
    
    def __right_child(self, i):
        return (i << 1) + 2
    
    # Here comes the good part
    def __max_heapify__(self, i):
        left_child = self.__left_child(i)
        right_child = self.__right_child(i)
        n = len(self.data)
        # Let me explain it here
        # ((left_child < n) and (self.data[left_child] > self.data[left_child])) ? left_child : i, OK?
        largest = ((left_child < n) and (self.data[left_child] > self.data[i])) and left_child or i
        largest = ((right_child < n) and (self.data[right_child] > self.data[largest])) and right_child or largest
        # Now we have the largest node
        if i != largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max_heapify__(largest)
        # Nice and neat, right?        

    def extract_max(self):
        n = len(self.data)
        if not n:
            print("Heap is empty!")
        else:
            val = self.data[0]
            # This is simple and smart
            self.data[0] = self.data[n-1]
            self.data.pop()
            self.__max_heapify__(0)
            return val

if __name__ == '__main__':
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print ("Tests Passed!")