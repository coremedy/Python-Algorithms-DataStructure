'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Stack

def dec2bin_with_stack(decnum):
    s = Stack()
    res = ''
    
    while decnum > 0:
        s.push(decnum % 2)
        decnum //= 2
    
    while not s.isEmpty():
        res += str(s.pop())
        
    return res
        
if __name__ == '__main__':
    decnum = 9
    assert(dec2bin_with_stack(decnum) == '1001')