'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def hash_func(astring, tablesize):
    Sum = 0
    for pos in range(len(astring)):
        Sum += ord(astring[pos])
    return Sum % tablesize

def find_anagram_hash_function(word1, word2):
    tablesize = 11
    return hash_func(word1, tablesize) == hash_func(word2, tablesize)

def test_find_anagram_hash_function(module_name='this module'):
    word1 = 'buffy'
    word2 = 'bffyu'
    word3 = 'bffya'
    word4 = 'acac'
    word5 = 'bbbb'
    assert(find_anagram_hash_function(word1, word2) == True)
    assert(find_anagram_hash_function(word1, word3) == False)
    '''
    You see the limitation here? Should this be true?
    '''
    assert(find_anagram_hash_function(word4, word5) == True)
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_find_anagram_hash_function()