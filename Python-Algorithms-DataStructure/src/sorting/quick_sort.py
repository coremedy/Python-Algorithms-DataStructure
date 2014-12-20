'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def quick_sort(seq):
    # baseline
    if len(seq) < 2:
        return seq
    pivot_index = (len(seq) - 1) // 2
    pivot = seq[pivot_index]
    # divide
    left = [x for i, x in enumerate(seq) if (x <= pivot) and (i != pivot_index)]
    right = [x for i, x in enumerate(seq) if (x > pivot) and (i != pivot_index)]
    # and merge
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_inplace(seq):
    # baseline
    if len(seq) <= 1:
        return seq
    if len(seq) == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq
    # not a good choice
    pivot = seq[0]
    ptr1, ptr2 = 1, len(seq) - 1
    while ptr1 < ptr2:
        if seq[ptr1] <= pivot:
            seq[ptr1], seq[ptr2] = seq[ptr2], seq[ptr1]
            ptr2 -= 1
        else:
            ptr1 += 1
    if seq[ptr1] <= pivot:
        ptr1 -= 1
    if ptr1 > 0:
        seq[0], seq[ptr1] = seq[ptr1], seq[0]
    return quick_sort_inplace(seq[ptr1 + 1:]) + [pivot] + quick_sort_inplace(seq[:ptr1])
    
if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq2 = [9, 7, 8, 6, 5, 2, 3, 1, 4]
    assert(quick_sort(seq) == sorted(seq))
    assert(quick_sort_inplace(seq2) == sorted(seq2))