'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import timeit
import random

if __name__ == '__main__':
    for i in range(10000,1000001,20000):
        t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random,x")
        x = list(range(i))
        '''
        Run the statement 'random.randrange(%d) in x' for 1000 times
        '''
        lst_time = t.timeit(number=1000)
        x = {j : None for j in range(i)}
        dic_time = t.timeit(number=1000)
        print("%d,%10.3f,%10.3f" % (i, lst_time, dic_time))