'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from functools import wraps

def memo(func):
    cache = {}
    
    # if wraps is used, fib can reserve its name
    @wraps(func)
    def wrap(*args):
        # the args here is a tuple
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrap

@memo
def fib(i):
    if i < 2: return 1
    return fib(i-1) + fib(i-2)

if __name__ == '__main__':
    print(fib(130))