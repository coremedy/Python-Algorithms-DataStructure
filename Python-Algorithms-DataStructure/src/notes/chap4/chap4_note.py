'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
import collections

if __name__ == '__main__':
    '''
    lambda : something like function objects (related to Functional Programming)
    '''
    area = lambda x, y: x * y * 0.5
    minus_one_dict = collections.defaultdict(lambda: -1)
    point_zero_dict = collections.defaultdict(lambda: (0, 0))
    message_dict = collections.defaultdict(lambda: "No message")
    
    testlist = []
    if testlist:
        print("Get U!")
    if testlist != []:
        print("Get U!")
        
    test = None
    if test:
        print("Get U!")
    if test is not None:
        print("Get U!")
        
        
    teststr = ''
    if teststr:
        print("Get U!")
    if teststr != '':
        print("Get U!")

    testdict = {}
    if testdict:
        print("Get U!")
    if testdict != {}:
        print("Get U!")
        
    print(None and False)
    print(None and True)
    print(None or False)
    print(None or True)