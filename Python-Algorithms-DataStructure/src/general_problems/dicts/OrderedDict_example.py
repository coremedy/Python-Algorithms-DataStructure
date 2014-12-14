'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
from collections import OrderedDict

def OrderedDict_example():
    pairs = [('c', 1), ('b',2), ('a',3)]
    
    d1 = {}
    
    for k, v in pairs:
        if k not in d1:
            d1[k] = []
        d1[k].append(v)
    
    for k in d1:
        print(k, d1[k])
    
    '''
    insertion order
    '''       
    d2 = OrderedDict(pairs)
    
    for k in d2:
        print(k, d2[k])
    

if __name__ == '__main__':
    OrderedDict_example()