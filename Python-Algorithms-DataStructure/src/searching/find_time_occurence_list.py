'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from searching.binary_search import binary_search_iter

def find_time_occurrence_list(seq, k):
    index_k = binary_search_iter(seq, k)
    count = 0
    if index_k == -1:
        return count
    size_seq = len(seq)
    
    for i in range(index_k, size_seq):
        if seq[i] == k:
            count += 1
        else:
            break
    
    for i in range(index_k - 1, -1, -1):
        if seq[i] == k:
            count += 1
        else:
            break
    
    return count        
    
if __name__ == '__main__':
    seq = [1,2,2,2,2,2,2,5,6,6,7,8,9]
    k = 2
    assert(find_time_occurrence_list(seq, k) == 6)
    print('Tests passed!')