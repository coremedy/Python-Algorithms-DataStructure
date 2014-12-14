'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from collections import Counter
from _collections import defaultdict

def find_dice_probabilities(S, n_faces=6):
    if (S < 2) or (S > 2 * n_faces):
        return None
    
    counter_dict = Counter()
    detail_dict = defaultdict(list)
    
    for dice1 in range(1, n_faces):
        for dice2 in range(1, n_faces):
            counter_dict[dice1 + dice2] += 1
            detail_dict[dice1 + dice2].append([dice1, dice2])
            
    return [counter_dict[S], detail_dict[S]]

def test_find_dice_probabilities(module_name='this module'):
    n_faces = 6
    S = 5
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert(results[0] == len(results[1]))
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))
            
if __name__ == '__main__':
    test_find_dice_probabilities()