'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def convert_from_decimal_larger_bases(number, base):
    strings = '0123456789ABCDEFGHIJ'
    result = ''
    while number > 0:
        result = strings[number % base] + result
        number //= base
    return result

def convert_from_decimal_larger_bases_rec(number, base):
    strings = '0123456789ABCDEFGHIJ'
    if number < base:
        return strings[number]
    else:
        return convert_from_decimal_larger_bases_rec(number // base, base) + strings[number % base]

def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == '1F')
    assert(convert_from_decimal_larger_bases_rec(number, base) == '1F')
    print('Test passed!')
    
if __name__ == '__main__':
    test_convert_from_decimal_larger_bases()