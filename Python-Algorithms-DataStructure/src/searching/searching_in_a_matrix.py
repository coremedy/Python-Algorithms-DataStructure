'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import numpy

def searching_in_a_matrix(m1, value):
    rows = len(m1)
    cols = len(m1[0])
    low = 0
    high = rows * cols - 1
    while low < high:
        mid = (low + high) // 2
        v =  m1[mid // cols][mid % cols]
        if v == value:
            return True
        elif v > value:
            high = mid - 1
        else:
            low = mid + 1
    if m1[low // cols][low % cols] == value:
        return True
    return False

if __name__ == '__main__':
    a = [[1,3,5],[7,9,11],[13,15,17]]
    b = numpy.array([(1,2),(3,4)])
    assert(searching_in_a_matrix(a, 13) == True)
    assert(searching_in_a_matrix(a, 14) == False)
    assert(searching_in_a_matrix(b, 3) == True)
    assert(searching_in_a_matrix(b, 5) == False)
    print('Tests passed!')