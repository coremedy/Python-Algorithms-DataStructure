'''
Created on 2014-12-15

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import os
import sys
import shutil

def change_file_ext():
    if len(sys.argv) <= 2:
        print("Usage: change_ext.py filename.old_ext 'new_ext'")
        sys.exit()
    
    '''
    old name plus new extension
    '''
    name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
    print(name)
    
    try:
        shutil.copy(sys.argv[1], name)
    except OSError as err:
        print (err)

if __name__ == '__main__':
    change_file_ext()