'''
Created on 2014-12-28

Code coming from: http://www.ibm.com/developerworks/library/l-prog/
'''

from functools import reduce

def do_something(i):
    print(i)
    # return None

if __name__ == '__main__':
    # while i < 5:
    #    print(i)
    #    i += 1
    i = 0
    while_fp = lambda i: (i < 5) and (do_something(i + 1) or while_fp(i + 1))
    print(while_fp(i))
    
    # res = []
    # xs = (1,2,3,4)
    # ys = (5,6,7,8)
    # for x in xs:
    #    for y in ys:
    #        if x * y > 25;
    #            res.append((x, y))
    bigmuls = lambda xs, ys: filter(lambda tup : tup[0] * tup[1] > 25, combine(xs ,ys))
    combine = lambda xs, ys: zip(xs * len(ys), dup_elements(ys, len(xs)))
    dup_elements = lambda lst, n: reduce(lambda s,t: s + t, map(lambda l,n=n: [l]*n, lst))
    print(list(bigmuls((1,2,3,4), (5,6,7,8))))