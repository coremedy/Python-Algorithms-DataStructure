'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def finding_gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return finding_gcd_rec(b, a % b)

def test_finding_gcd_rec():
    number1 = 21
    number2 = 12
    assert(finding_gcd_rec(number1, number2) == 3)
    print('Tests passed!')

if __name__ == '__main__':
    test_finding_gcd_rec()