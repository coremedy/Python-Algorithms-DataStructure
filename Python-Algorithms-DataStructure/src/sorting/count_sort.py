'''
Created on 2014-12-19

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from collections import defaultdict

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