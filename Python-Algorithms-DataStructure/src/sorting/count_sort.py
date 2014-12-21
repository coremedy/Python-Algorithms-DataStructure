'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from collections import defaultdict

def counting_sort_age(A):
    timesOfAge = [0] * 100
    # set is actually not ordered
    ageCountSet = set()
    B = []
    for i in A:
        timesOfAge[i] += 1
        ageCountSet.add(i)
    for j in ageCountSet:
        count = timesOfAge[j]
        while count:
            B.append(j)
            count -= 1
    return B

def count_sort_dict(a):
    r, d = [], defaultdict(list)
    for x in a:
        d[x].append(x)
    for x in range(min(d), max(d) + 1):
        r.extend(d[x])
    return r

if __name__ == '__main__':
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(count_sort_dict(seq) == sorted(seq))
    print('Tests passed!')
    print(counting_sort_age(seq))