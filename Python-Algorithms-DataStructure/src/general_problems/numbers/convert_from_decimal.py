'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while (number > 0):
        result += (number % base) * multiplier
        multiplier *= 10
        number //= base
    return result

def convert_from_decimal_rec(number, base, multiplier):
    if number < base:
        return number * multiplier
    else:
        return (number % base) * multiplier + convert_from_decimal_rec(number // base, base, multiplier * 10)

def test_covert_from_decimal():
    number, base = 21, 2
    assert(convert_from_decimal(number, base) == 10101)
    assert(convert_from_decimal_rec(number, base, 1) == 10101)
    print("Test passed!")

if __name__ == '__main__':
    test_covert_from_decimal()