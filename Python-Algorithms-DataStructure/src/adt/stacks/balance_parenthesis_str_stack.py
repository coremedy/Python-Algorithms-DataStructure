'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from adt.stacks.stack import Stack

def balance_par_str_with_stack(str1):    
    s = Stack()
    balanced = True
    index = 0
    
    while (index < len(str1)) and balanced:        
        if str1[index] == '(':
            s.push('(')
        else:
            # important
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    
    if s.isEmpty() and balanced:
        return True
    else:
        return False
        
if __name__ == '__main__':
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
    print(balance_par_str_with_stack(')('))