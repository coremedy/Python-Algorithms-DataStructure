'''
Created on 2014-12-21

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def bubble_sort(seq):
    size_ = len(seq) - 1
    for num in range(size_, 0, -1):
        for i in range(num):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq 

if __name__ == '__main__':
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(bubble_sort(seq) == sorted(seq))
    print('Tests passed!')