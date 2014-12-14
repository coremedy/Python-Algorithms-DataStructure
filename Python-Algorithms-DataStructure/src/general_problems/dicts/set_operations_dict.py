'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from collections import OrderedDict

def set_operations_with_dict():
    '''
    This is a list
    '''
    pairs = [('a', 1), ('b',2), ('c',3)]
    d1 = OrderedDict(pairs)
    print(d1)
    
    d2 = {'a': 1, 'c': 2, 'd': 3, 'e': 4}
    print(d2)
    
    print(d1.keys() & d2.keys())
    print(d1.keys() | d2.keys())
    print(d1.keys() - d2.keys())
    
    d3 = { key : d2[key] for key in d2.keys() - {'c', 'd'}}
    print(d3)

if __name__ == '__main__':
    set_operations_with_dict()