'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while (j > 0) and (seq[j - 1] > seq[j]):
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1 
    return seq

def insertion_sort_rec(seq, i = None):
    # initial
    if i is None:
        i = len(seq) - 1
    # baseline
    if i == 0:
        return None
    # divide the problem into 0 - (len(seq) - 2) and len(seq) - 1
    insertion_sort_rec(seq, i - 1)
    # then process the last piece
    while (i > 0) and (seq[i - 1] > seq[i]):
        seq[i - 1], seq[i] = seq[i], seq[i - 1]
        i -= 1
    return seq

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(insertion_sort(seq) == sorted(seq))
    assert(insertion_sort_rec(seq) == sorted(seq))
    print('Tests passed!')