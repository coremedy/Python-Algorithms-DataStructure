'''
Created on 2014-12-22

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def ordered_sequential_search(seq, n):
    for item in seq:
        if item > n:
            return False
        if item == n:
            return True
    return False

def test_ordered_sequential_search(module_name='this module'):
    seq = [1, 2, 4, 5, 6, 8, 10]
    n1 = 10
    n2 = 7
    assert(ordered_sequential_search(seq, n1) == True)
    assert(ordered_sequential_search(seq, n2) == False)
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_ordered_sequential_search()