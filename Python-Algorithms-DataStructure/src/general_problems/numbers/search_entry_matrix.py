'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def find_elem_matrix_bool(m1, value):
    row = 0
    col = len(m1[0]) - 1
    while (row < len(m1)) and (col >= 0):
        if m1[row][col] == value:
            return True
        elif m1[row][col] > value:
            col -= 1
        else:
            row += 1
    return False

if __name__ == '__main__':
    m1 = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
    assert(find_elem_matrix_bool(m1,8) == True)
    assert(find_elem_matrix_bool(m1,3) == False)
    m2 = [[0]]
    assert(find_elem_matrix_bool(m2,0) == True)