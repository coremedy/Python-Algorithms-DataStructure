'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

from pip._vendor.requests.packages.urllib3.connectionpool import xrange
import math

'''
https://pyzh.readthedocs.org/en/latest/the-python-yield-keyword-explained.html
'''
def primes_sieve_list(limit):
    sieve = [True] * limit
    '''
    print(sys.getsizeof(sieve))
    '''
    sieve[0] = sieve[1] = False
    
    for (i, isPrime) in enumerate(sieve):
        if isPrime:
            yield i
            for n in xrange(i * i, limit, i):
                sieve[n] = False
                
def test_primes_sieve_list():
    '''
    Interesting here. Use a generator and get the value one by one, avoiding creating large lists
    '''
    generator = primes_sieve_list(100)
    assert(next(generator) == 2)
    assert(next(generator) == 3)
    assert(next(generator) == 5)
    print('Tests passed!')
    
def primes_sieve_set(limit):
    multiples = set()
    for i in xrange(2, limit + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, limit + 1, i))
            
def test_primes_sieve_set():
    '''
    Interesting here. Use a generator and get the value one by one, avoiding creating large lists
    '''
    generator = primes_sieve_set(100)
    assert(next(generator) == 2)
    assert(next(generator) == 3)
    assert(next(generator) == 5)
    print('Tests passed!')
    
def find_prime_sqrt_brute_force(number):
    num = abs(number)
    if (num == 3) or (num == 2):
        return True
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False
        return True
    
def test_find_prime_sqrt_brute_force():
    assert(find_prime_sqrt_brute_force(2))
    assert(find_prime_sqrt_brute_force(3))
    assert(find_prime_sqrt_brute_force(18) == False)
    print('Tests passed!')

if __name__ == '__main__':
    test_primes_sieve_list()
    test_primes_sieve_set()
    test_find_prime_sqrt_brute_force()