'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import string
from collections import deque
from adt.queues.dequeue import Deque

STRIP = string.whitespace + string.punctuation + "\"'`"

def palindrome_checker_with_deque(str1):
    d1 = Deque()
    d2 = deque()
    
    for ch in str1.lower():
        if ch not in STRIP:
            d1.enqueue_right(ch)
            d2.append(ch)
    
    # check d1
    eq1 = True
    while (d1.size() > 1) and eq1:
        if d1.dequeue_left() != d1.dequeue_right():
            eq1 = False
            
    # check d2
    eq2 = True
    while len(d2) > 1 and eq2:
        if d2.pop() != d2.popleft():
            eq2 = False
            
    return eq1, eq2

if __name__ == '__main__':
    str1 = 'Madam Im Adam'
    str2 = 'Buffy is a Slayer'
    print(palindrome_checker_with_deque(str1))
    print(palindrome_checker_with_deque(str2))