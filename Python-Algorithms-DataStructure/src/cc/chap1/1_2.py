'''
Created on 2015-07-06

Question: Implement a (C/C++) function which reverses a (NULL terminated) string
'''

def reverse(source_str):
    if source_str is None:
        return source_str
    source_str_length = len(source_str)
    if source_str_length <= 1:
        return source_str
    # Python strings are immutable
    mutable_str = bytearray(source_str, 'ascii')
    for index in range(0, source_str_length // 2):
        (mutable_str[index], mutable_str[source_str_length - 1 - index]) = (mutable_str[source_str_length - 1 - index], mutable_str[index])
    return mutable_str.decode(encoding='ascii')

if __name__ == '__main__':
    print(reverse('1234567890'))