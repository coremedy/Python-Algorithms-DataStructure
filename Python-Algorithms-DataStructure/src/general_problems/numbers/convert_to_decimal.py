'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

'''
An interesting function, converting the number, such as 101101 (2 based) into decimal
The number here is not a string, it is actually a decimal ...
'''

def covert_to_decimal(number, base):
    multiplier, result = 1, 0
    while (number > 0):
        result += (number % 10) * multiplier
        multiplier *= base
        number //= 10
    return result

def covert_to_decimal_rec(number, base, multiplier):
    if number < base:
        return number * multiplier
    else:
        return (number % 10) * multiplier + covert_to_decimal_rec(number // 10, base, multiplier * base)

def test_covert_to_decimal():
    '''
    The result should be 21 ....
    You see the meaning of the number here?
    '''
    number, base = 10101, 2
    assert(covert_to_decimal(number, base) == 21)
    assert(covert_to_decimal_rec(number, base, 1) == 21)
    print("Test passed!")
    
if __name__ == '__main__':
    test_covert_to_decimal()