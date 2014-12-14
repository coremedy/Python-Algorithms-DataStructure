'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
from _collections import defaultdict

def defaultdict_example():
    pairs = {('a', 1), ('b', 2), ('c', 3)}
    d1 = {}
    
    for k, v in pairs:
        if k not in d1:
            d1[k] = []
        d1[k].append(v)
    print(d1)
    
    '''
    actually default value is set here
    '''
    d2 = defaultdict(list)
        
    for k, v in pairs:
        d2[k].append(v)
    print(d2)

if __name__ == '__main__':
    defaultdict_example()