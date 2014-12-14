'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
import string

def verify_two_strings_are_anagrams(str1, str2):
    ana_table = {key:0 for key in string.ascii_lowercase}
    
    for ch in str1.lower():
        ana_table[ch] += 1
    
    for ch in str2.lower():
        ana_table[ch] -= 1
    
    '''
    Should be a set containing only zero if two strs are anagrams
    '''
    if len(set(ana_table.values())) < 2:
        return True
    else: 
        return False
        
def test_verify_two_strings_are_anagrams():
    str1 = 'marina'
    str2 = 'aniram'
    assert(verify_two_strings_are_anagrams(str1, str2) == True)
    str1 = 'google'
    str2 = 'gouglo'
    assert(verify_two_strings_are_anagrams(str1, str2) == False)
    print('Tests passed!')

if __name__ == '__main__':
    test_verify_two_strings_are_anagrams()