'''
Created on 2014-12-17

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import heapq

def merge_sorted_seqs(seq1, seq2):
    result = []
    # iterator
    for c in heapq.merge(seq1, seq2):
        result.append(c)
    return result

def test_merge_sorted_seq(module_name='this module'):
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert(merge_sorted_seqs(seq1, seq2) == sorted(seq3))
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_merge_sorted_seq()