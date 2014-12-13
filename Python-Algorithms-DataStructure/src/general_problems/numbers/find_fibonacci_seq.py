'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import math

def find_fibonacci_seq_dp(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_dp(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print('Tests passed!')

if __name__ == '__main__':
    test_find_fib()