'''
Created on 2015-07-06

Question: Write a method to replace all spaces in a string with '%20'. 
          You may assume that the string has sufficient space at the end of the string to hold the additional characters, 
          and that you are given the "true" length of the string.
'''

def replaceSpaces(source_str):
    if source_str is None:
        return source_str
    if len(source_str) == 0:
        return source_str
    byte_array = bytearray(source_str, 'ascii')
    for index in range(0, len(source_str)):
        if source_str[index].isspace():
            byte_array.extend([0, 0])
    # Space is enough
    end_index = len(byte_array) - 1
    for index in range(len(source_str) - 1, -1, -1):
        if source_str[index].isspace():
            byte_array[end_index] = 48
            byte_array[end_index - 1] = 50
            byte_array[end_index - 2] = 37
            end_index -= 3
        else:
            byte_array[end_index] = ord(source_str[index])
            end_index -= 1
    return byte_array.decode(encoding='ascii')

if __name__ == '__main__':
    print(replaceSpaces('Hello World    Hey  '))