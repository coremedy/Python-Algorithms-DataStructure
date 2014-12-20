'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def siftdown(seq, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and seq[child] < seq[child + 1]:
            child += 1
        if seq[root] < seq[child]:
            seq[root], seq[child] = seq[child], seq[root]
            root = child
        else:
            break

def heap_sort3(seq):
    # create a max heap (heapify)
    for start in range((len(seq)-2)//2, -1, -1):
        siftdown(seq, start, len(seq)-1)
    # then, move the largest element to the end of the list
    # and re-heapify 0 to end - 1 (without considering the last element)
    for end in range(len(seq)-1, 0, -1):
        seq[end], seq[0] = seq[0], seq[end]
        siftdown(seq, 0, end - 1)
    return seq

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(heap_sort3(seq) == sorted(seq))
    print('Tests passed!')