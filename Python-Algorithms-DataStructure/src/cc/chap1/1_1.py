'''
Created on 2015-07-05

Question: Implement an algorithm to determine if a string has all unique characters.
          What if you cannot use additional data structure?
'''

# The first point is: ASCII or UNICODE
# Let us assume that the character is ASCII
def check_unique_character(target_str):
    # A simple kind of hashing table
    if target_str is None:
        return False
    target_str_len = len(target_str)
    if target_str_len == 0:
        return False
    book_mark = [False for dummy_i in range(0, 256)]
    for index in range(0, target_str_len):
        char_ord = ord(target_str[index])
        if book_mark[char_ord]:
            return False
        else:
            book_mark[char_ord] = True
    return True

# It is better to restrict the bitmap to a DWORD (less than 32 bit)
def check_unique_character_bitmap(target_str):
    if target_str is None:
        return False
    target_str_len = len(target_str)
    if target_str_len == 0:
        return False
    boundary = [(32 * dummy_i) for dummy_i in range(0, 9)]
    bitmap = [0 for dummy_i in range(0, 8)]
    for index in range(0, target_str_len):
        char_ord = ord(target_str[index])
        (bitmap_index, value) = find_the_closest_dword(char_ord, boundary)
        if (value & bitmap[bitmap_index] != 0):
            return False
        else:
            bitmap[bitmap_index] |= value
    return True

# Binary search
def find_the_closest_dword(char_ord, boundary):
    (begin, end, middle) = (0, len(boundary) - 1, (len(boundary) - 1) // 2)
    while (middle != begin):
        if char_ord < boundary[middle]:
            end = middle
        else:
            begin = middle
        middle = (begin + end) // 2
    return (begin, 1 << (char_ord - boundary[begin]))

if __name__ == '__main__':
    print(check_unique_character_bitmap('12345'))
    print(check_unique_character_bitmap('123451'))