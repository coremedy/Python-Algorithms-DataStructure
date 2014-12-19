'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

# Additional space will be used, but the complexity is good
# If in-place is needed (no additional space), the complexity will be greater than O(nlgn)
def merge_sort(seq):
    # baseline
    if len(seq) == 1:
        return seq
    if len(seq) == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq
    # divide
    mid_index = (len(seq) - 1) // 2 + 1
    left = merge_sort(seq[:mid_index])
    right = merge_sort(seq[mid_index:])
    # conquer 
    res = []
    # If you use pop(1) here the complexity will increase
    # here I think the complexity should be O(2n)
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    assert(merge_sort(seq) == seq_sorted)