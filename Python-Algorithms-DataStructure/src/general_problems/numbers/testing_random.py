'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import random
def testing_random():
    ''' testing the module random'''
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    
    ''' create list '''
    print(random.sample(values, 2))
    print(random.sample(values, 3))
    
    ''' shuffle in place '''
    random.shuffle(values)    
    print(values)
    
    ''' create random integers '''
    print(random.randint(0,10))
    print(random.randint(0,10))

if __name__ == '__main__':
    testing_random()