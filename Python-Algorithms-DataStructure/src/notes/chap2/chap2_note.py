'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
import decimal


'''
sequence types
immutable: tuple, strings and bytes
mutable: lists and byte arrays
'''

if __name__ == '__main__':
    B = bytes([0x1f, 0x1e])
    BB = bytes('example', encoding = "utf8")
    print(repr(B))
    print(repr(BB))
    print(type(B))
    
    '''
    Return a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256
    '''
    BA = bytearray('example', encoding = "utf8")
    print(repr(BA))
    '''
    chr/ord
    '''
    BA[0] = ord('E')
    print(repr(BA))
    
    '''
    set (not a sequence type, just need to demostrate the deep-copy)
    '''
    S = {'Alex', 'Betty', 'Clark'}
    AnotherS = S.copy()
    
    strin = 'I am a string'
    print(''.join(reversed(strin)))
    print(strin.rjust(50, '-'))
    print(strin.ljust(50, '-'))
    
    print("The {who} was {0} last week".format(12, who="boy"))
    '''
    to force string form, r to force representational form, and a to force representational form but only using ASCII characters:
    '''
    print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))
    '''
    How to print local variables efficiently
    '''
    print('{strin} plus {S}'.format(**locals()))
    print(strin.split(' '))
    
    slayers = "Buffy and Faith"
    print(slayers.swapcase())
    print(slayers.upper())
    print(slayers.lower())
    print(slayers.find('h'))
    print(slayers.index('u'))
    print(slayers.count('f', 0, len(slayers) - 1))
    
    slayer2 = "Buffy is Buffy is Buffy"
    print(slayer2.replace("Buffy", "Tuffy", 2))
    
    t = (1, 5, 7, 8, 9, 4, 1, 4)
    print(len(t))
    print(t.count(4))
    
    '''
    unpacking
    '''
    x, *y = (1, 2, 3, 4)
    print(x)
    print(y)
    