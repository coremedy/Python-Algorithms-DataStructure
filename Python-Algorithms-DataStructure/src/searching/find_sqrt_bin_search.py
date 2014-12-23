'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def find_sqrt_bin_search(n, error=0.001):
    low = n < 1 and 0 or 1
    high = n < 1 and 1 or n
    
    mid = low + (high - low) / 2.0
    square = mid * mid
    
    while abs(square - n) > error:
        if square < n:
            low = mid
        else:
            high = mid
        mid = low + (high - low) / 2.0
        square = mid * mid
        
    return mid

if __name__ == '__main__':
    number = 9
    assert(find_sqrt_bin_search(number) == 3)
    print('Tests passed!')