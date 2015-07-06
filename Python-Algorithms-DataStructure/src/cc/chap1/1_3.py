'''
Created on 2015-07-06

Question: Given two strings, write a method to decide one is a permutation of the other
'''

import collections

# Sorting
def is_permutation(s1, s2):
    if (s1 is None) and (s2 is None):
        return True
    if (s1 is not None) and (s2 is not None):
        if len(s1) != len(s2):
            return False
        return ((sorted(list(s1))) == (sorted(list(s2))))
    return False

# Character count    
def is_permutation_ctr(s1, s2):
    if (s1 is None) and (s2 is None):
        return True
    if (s1 is not None) and (s2 is not None):
        if len(s1) != len(s2):
            return False
        return (collections.Counter(s1) == collections.Counter(s2))
    return False        
    
if __name__ == '__main__':
    print(is_permutation('4321', '1234'))
    print(is_permutation_ctr('4321', '1334'))