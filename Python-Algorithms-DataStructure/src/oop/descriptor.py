'''
Created on 2014-12-15

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

'''
For member variables like __name, how to access it without 'calling' getter/setter?
'''

class Person(object):
    def __init__(self):
        self.__name = ''

    def fget(self):
        print("Getting: %s" % self.__name)
        return self.__name
    
    def fset(self, value):
        print("Setting: %s" % value)
        self.__name = value.title()

    def fdel(self):
        print("Deleting: %s" % self.__name)
        del self.__name
        
    name = property(fget, fset, fdel, "I'm the property.")
    
class Person2(object):
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        print("Getting: %s" % self.__name)
        return self.__name
    
    @name.setter
    def name(self, value):
        print("Setting: %s" % value)
        self.__name = value.title()

    @name.deleter
    def name(self):
        print("Deleting: %s" % self.__name)
        del self.__name   

if __name__ == '__main__':
    p = Person()
    p.name = "Alex"
    print(p.name)
    del p.name
    
    p = Person2()
    p.name = "Alex"
    print(p.name)
    del p.name