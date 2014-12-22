'''
Created on 2014-12-22

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from numpy import median

def quickSelect(seq, k):
    length = len(seq)
    # baseline
    if not length:
        return None
    if length == 1:
        return seq[0]
    # find pivot
    pivot_index = length // 2
    pivot = seq[pivot_index]    
    small = [x for i, x in enumerate(seq) if x <= pivot and i != pivot_index]
    large = [x for i, x in enumerate(seq) if x > pivot and i != pivot_index]
    
    length_small = len(small)
    if k == length_small:
        return pivot
    elif k < length_small:
        return quickSelect(small, k)
    else:
        return quickSelect(large, k - length_small - 1)
    
def quickSelectHard(seq, k, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(seq) - 1
    pivot_index = left + (right - left + 1) // 2 
    pivot = seq[pivot_index]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    
    swap_index, i = left, left
    while i < right:
        if seq[i] < pivot:
            seq[i], seq[swap_index] = seq[swap_index], seq[i]
            swap_index += 1
        i += 1
    seq[swap_index], seq[right] = seq[right], seq[swap_index]
    
    if k == swap_index:
        return seq[swap_index]
    elif k < swap_index:
        return quickSelectHard(seq, k, left, swap_index - 1)
    else:
        return quickSelectHard(seq, k, swap_index + 1, right)
    
if __name__ == '__main__':
    for k in range(len([10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200])):
        assert(quickSelect([10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200], k) == quickSelectHard([10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200], k))
    print(median([10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200]))