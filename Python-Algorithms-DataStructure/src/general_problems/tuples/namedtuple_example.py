'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
from collections import namedtuple

def namedtuple_example():
    '''
    like enum?
    The First argument to collections.namedtuple is the name of the custom tuple data type to be created.
    The second argument is a string of space-separated names, one for each item that the custom tuple will take.
    '''
    datatype = namedtuple('name', ['job', 'age'])
    tup = datatype('engineer', 27)
    print(tup.job)
    print(tup.age)
    

if __name__ == '__main__':
    namedtuple_example()