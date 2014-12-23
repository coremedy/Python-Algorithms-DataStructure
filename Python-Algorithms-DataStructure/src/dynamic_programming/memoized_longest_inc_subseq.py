'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from dynamic_programming.memo import memo
from itertools import combinations
from bisect import bisect
from oop.do_benchmark import benchmark

# bottom-up dp
def longest_inc_subseq_iter_dp(seq):
    L = [1] * len(seq)
    # sub problems - LIS of 0 - i ending at seq[i]
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], L[pre] + 1)
    # final decision
    return max(L)

# memorization dp
def memoized_longest_inc_subseq_dp(seq):    
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    
    return max(L(i) for i in range(len(seq)))

# interesting 
def longest_inc_subseq_bisect(seq):
    L = []
    # the length of the LIS is kept
    # but the content of L may not be correct
    for val in seq:
        ind = bisect(L, val)
        if ind == len(L):
            L.append(val)
        else:
            L[ind] = val
    return len(L)

# naive 2^n
def naive_longest_inc_subseq(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(list(sub)):
                return len(sub)


@benchmark
def test_naive_longest_inc_subseq():
    print(naive_longest_inc_subseq([42, 57, 99, 65, 30, 75, 89, 63, 75, 50, 9, 21, 75, 3, 15, 16, 43, 79, 27, 45, 74, 36, 36, 7, 81, 36, 76, 69, 80, 63, 24, 75, 41, 5, 17, 81, 53, 64, 36, 82]))

@benchmark
def test_longest_inc_subseq_iter_dp():
    print(longest_inc_subseq_iter_dp([42, 57, 99, 65, 30, 75, 89, 63, 75, 50, 9, 21, 75, 3, 15, 16, 43, 79, 27, 45, 74, 36, 36, 7, 81, 36, 76, 69, 80, 63, 24, 75, 41, 5, 17, 81, 53, 64, 36, 82]))

@benchmark
def test_longest_inc_subseq_bisect():
    print(longest_inc_subseq_bisect([42, 57, 99, 65, 30, 75, 89, 63, 75, 50, 9, 21, 75, 3, 15, 16, 43, 79, 27, 45, 74, 36, 36, 7, 81, 36, 76, 69, 80, 63, 24, 75, 41, 5, 17, 81, 53, 64, 36, 82]
))

@benchmark
def test_memorized_longest_inc_subseq_dp():
    print(memoized_longest_inc_subseq_dp([42, 57, 99, 65, 30, 75, 89, 63, 75, 50, 9, 21, 75, 3, 15, 16, 43, 79, 27, 45, 74, 36, 36, 7, 81, 36, 76, 69, 80, 63, 24, 75, 41, 5, 17, 81, 53, 64, 36, 82]))

if __name__ == '__main__':
    test_longest_inc_subseq_bisect()
    test_longest_inc_subseq_iter_dp()
    test_memorized_longest_inc_subseq_dp()
    # Take care here
    test_naive_longest_inc_subseq()