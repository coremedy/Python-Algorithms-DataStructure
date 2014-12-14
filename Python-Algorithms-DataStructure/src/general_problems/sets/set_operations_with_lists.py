'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''


def list_remove_duplicate(l):
    return list(set(l))

def list_intersection(l1, l2):
    return list(set(l1).intersection(set(l2)))

def list_union(l1, l2):
    return list(set(l1).union(set(l2)))

def test_sets_operations_with_lists():
    l1 = [1,2,3,4,5,9,11,15]
    l2 = [4,5,6,7,8]
    l3 = []
    
    assert(list_remove_duplicate(l1) == [1, 2, 3, 4, 5, 9, 11, 15])
    assert(list_remove_duplicate(l2) == [8, 4, 5, 6, 7])
    assert(list_intersection(l1, l2) == [4,5])
    assert(list_union(l1, l2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15])
    assert(list_remove_duplicate(l3) == [])
    assert(list_intersection(l3, l2) == l3)
    assert(sorted(list_union(l3, l2)) == sorted(l2))
    print('Tests passed!')

if __name__ == '__main__':
    test_sets_operations_with_lists()