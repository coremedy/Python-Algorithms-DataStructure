'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from collections import Counter

def find_top_N_recurring_words(seq, N):
    dcounter = Counter()
    for word in seq.split():
        dcounter[word] += 1
    return dcounter.most_common(N)

def test_find_top_N_recurring_words(module_name='this module'):
    seq = 'buffy angel monster xander a willow gg buffy the monster super buffy angel'
    N = 3
    '''
    Do not use list comparison here since ... the element is tuple
    change it to set
    '''
    assert(set(find_top_N_recurring_words(seq, N)) == set([('buffy', 3),('angel', 2),('monster', 2)]))
    print('Tests in {name} have {con}!'.format(name=module_name, con='passed'))
    
if __name__ == '__main__':
    test_find_top_N_recurring_words()