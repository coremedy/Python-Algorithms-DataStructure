'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import numpy
import time

def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    '''
    In Python 3.3, map returns an iterator, if your function expects a list, that has to be explicitly converted. like this
    next(map(sum, zip(X,Y)))
    '''
    Z = list(map(sum, zip(X,Y)))
    t2 = time.time()
    return t2 - t1

def numpy_version():
    t1 = time.time()
    X = numpy.arange(10000000)
    Y = numpy.arange(10000000)
    Z = X + Y
    t2 = time.time()
    return t2 - t1

if __name__ == '__main__':
    print(trad_version())
    print(numpy_version())