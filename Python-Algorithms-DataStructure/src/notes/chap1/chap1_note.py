'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

'''
An interesting function, coverting the number, such as 101101 (2 based) into decimal
The number here is not a string, it is actually a decimal ...
'''

import struct
from decimal import Decimal
from fractions import Fraction

if __name__ == '__main__':
    '''
    The length of integer will increase dynamically
    And integer is immutable
    '''
    print(int(1234567890123456).bit_length())
    a = 12345
    print(id(a))
    a += 54321
    print(id(a))
    
    '''
    The best way to compare floats is to convert them into binary representation first
    '''
    print(repr(struct.pack('>f', 123.456789)))
    print(struct.calcsize('f'))
    print(struct.calcsize('d'))
    
    '''
    Round function is not always reliable
    '''
    print(round(0.5))
    print(round(-0.6))
    '''
    Oops
    '''
    print(round(2.675, 2))
    '''
    Get quotient and remainder for division (tuple)
    '''
    print(divmod(7, 5))
    
    '''
    Get the integer fractional representation of a float
    '''
    print(2.5.as_integer_ratio())
    '''
    Oops
    '''
    print(2.333333333333333333333333333333333333333.as_integer_ratio())
    
    '''
    There is a Fraction class to handle rational number
    '''
    print(Fraction(-2, 10))
    
    '''
    In this case, you will know that python will handle the addition of floats via a binary manner
    Which cannot be understood by humans
    So, use Decimal to understand that'''
    print(sum(0.1 for i in range(10)))
    print(sum(Decimal('0.1') for i in range(10)))