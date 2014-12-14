'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
from collections import Counter

def Counter_example():
    seq1 = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]
    seq_counts = Counter(seq1)
    print(seq_counts)
    
    '''
    add more things
    '''
    seq2 = [1, 2, 3]
    seq_counts.update(seq2)
    print(seq_counts)
    
    seq3 = [1, 4, 3]
    for key in seq3:
        seq_counts[key] += 1
    print(seq_counts)
    
    '''
    This is really useful
    Set operations
    '''
    seq_counts_2 = Counter(seq3)
    print(seq_counts_2)
    print(seq_counts + seq_counts_2)
    print(seq_counts - seq_counts_2)

if __name__ == '__main__':
    Counter_example()