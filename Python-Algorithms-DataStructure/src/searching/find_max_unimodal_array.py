'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def find_max_unimodal_array(A):
    # at least 3 elements
    if len(A) <= 2:
        return None
    left = 0
    right = len(A) - 1
    while right > left + 1:
        mid = (left + right) // 2
        if (A[mid - 1] < A[mid]) and (A[mid] > A[mid + 1]):
            return mid
        elif (A[mid - 1] < A[mid]) and (A[mid] < A[mid + 1]):
            left = mid
        else:
            right = mid
    return None

if __name__ == '__main__':
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    assert(find_max_unimodal_array(seq) == 6)
    print('Tests passed!')