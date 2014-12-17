'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Stack

def reverse_string_with_stack(str1):
    s = Stack()
    res = ''
    
    for ch in str1:
        s.push(ch)
    
    while not s.isEmpty():
        res += s.pop()
        
    return res

if __name__ == '__main__':
    str1 = 'Buffy is a Slayer!'
    print(str1)
    print(reverse_string_with_stack(str1))