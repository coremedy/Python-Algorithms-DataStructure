'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def selection_sort(seq):
    for i in range(len(seq) - 1, -1, -1):
        for j in range(i):
            if seq[j] > seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
    return seq

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(selection_sort(seq) == sorted(seq))
    print('Tests passed!')