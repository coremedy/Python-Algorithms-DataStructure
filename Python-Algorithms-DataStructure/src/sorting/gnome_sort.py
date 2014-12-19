'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if (not i) or (seq[i-1] <= seq[i]):
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(gnome_sort(seq) == sorted(seq))
    print('Tests passed!')