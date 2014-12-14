'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import string

def delete_unique_word(str1):
    m = {key : 0 for key in string.ascii_lowercase}
    
    for ch in str1.lower():
        m[ch] += 1
    
    for k in m:
        if m[k] > 1:
            str1 = str1.replace(k, '')
    
    return str1

def test_delete_unique_word():
    str1 = "google"
    assert(delete_unique_word(str1) == 'le')
    print('Tests passed!')

if __name__ == '__main__':
    test_delete_unique_word()