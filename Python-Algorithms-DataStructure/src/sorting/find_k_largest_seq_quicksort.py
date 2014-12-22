'''
Created on 2014-12-21

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import random

def qselect(A, k, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(A) - 1
    pivot_index = random.randint(left, right)
    pivot = A[pivot_index]
    
    A[pivot_index], A[right] = A[right], A[pivot_index]
    swapIndex, i = left, left
    while i <= right - 1:
        if A[i] < pivot:
            A[swapIndex], A[i] = A[i], A[swapIndex]
            swapIndex += 1
        i += 1
    A[swapIndex], A[right] = A[right], A[swapIndex]
    
    rank = len(A) - swapIndex
    if k == rank:
        return A[swapIndex]
    elif k < rank:
        return qselect(A, k, swapIndex + 1, right)
    else:
        return qselect(A, k, left, swapIndex - 1)
    
def find_k_largest_seq_quickselect(seq, k):
    kth_largest = qselect(seq, k)
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result

if __name__ == '__main__':
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 2
    assert(find_k_largest_seq_quickselect(seq,k) == [10, 11])