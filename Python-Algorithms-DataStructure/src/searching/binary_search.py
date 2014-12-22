'''
Created on 2014-12-22

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from bisect import bisect

def binary_search_rec(seq, key, begin = 0):
    if not seq:
        return -1
    mid = len(seq) // 2
    if key == seq[mid]:
        return (mid + begin)
    elif key < seq[mid]:
        return binary_search_rec(seq[:mid], key, begin)
    else:
        return binary_search_rec(seq[mid + 1:], key, mid + 1)
    
def binary_search_iter(seq, key):
    begin, end = 0, len(seq) - 1
    while begin < end:
        mid = (begin + end) // 2
        if key == seq[mid]:
            return mid
        elif key > seq[mid]:
            begin = mid + 1
        else:
            end = mid - 1
    if key == seq[begin]:
        return begin
    return -1

if __name__ == '__main__':
    seq = [1,2,5,6,7,10,12,12,14,15]
    key = 6
    assert(binary_search_iter(seq, key) == 3)
    assert(binary_search_rec(seq, key) == 3)
    assert(bisect(seq, key) - 1 == 3)
    print('Tests passed!')