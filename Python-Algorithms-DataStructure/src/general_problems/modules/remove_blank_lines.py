'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import os
import sys

def read_data(filename):
    lines = []
    file_handle = None
    try:
        file_handle = open(filename)
        for line in file_handle:
            '''
            which means if line.strip() != '':
            '''
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if file_handle is not None:
            file_handle.close()
    return lines

def write_data(filename, lines):
    file_handle = None
    try:
        '''
        an existing le with the same name will be erased
        '''
        file_handle = open(filename, 'w')
        for line in lines:
            file_handle.write(line)
    except (EnvironmentError) as err:
        print(err)
    finally:
        if file_handle is not None:
            file_handle.close()

def remove_blank_lines(filename):
    lines = read_data(filename)
    '''
    which means if lines != []:
    '''    
    if lines:
        write_data(filename, lines)

if __name__ == '__main__':
    remove_blank_lines("C:\\test.txt")