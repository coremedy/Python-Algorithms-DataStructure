'''
Created on 2014-12-15

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import math

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
    
    '''
    override
    '''
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    '''
    override
    '''
    def __repr__(self):
        return "point ({0.x!r}, {0.y!r})".format(self)
    
    '''
    override
    '''
    def __str__(self):
        return repr(self)

class Circle(Point):
    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x, y)
        self.radius = radius
        
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2 * math.pi * self.radius

    '''
    override
    '''
    def __eq__(self, other): # avoid infinite recursion
        return self.radius == other.radius and super().__eq__(other)

    '''
    override
    '''
    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)
    
    '''
    override
    '''
    def __str__(self):
        return repr(self)
    
'''
Singleton, with __new__
'''
    
class Singleton(object):
    __singleton = None
    
    '''
    move your initializing code into the __new__
    *args and **kwargs allows that function to accept an arbitrary number of arguments and/or keyword arguments.
    '''
    def __new__(self, *args, **kwargs):
        if self.__singleton is None:
            self.__singleton = super(Singleton, self).__new__(self, *args, **kwargs)
        return self.__singleton

'''
Singleton, with decorator
'''    
def singleton_decorator(class_):
    instances = {}
    
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    
    return getinstance

@singleton_decorator
class MyClass(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

'''
Singleton, with metaclass
https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/
'''

class singleton_meta(type):
    __instance = {}
    
    def __new__(self, *args, **kwargs):
        print('-----------------------------------')
        print("Allocating memory for class")
        print(repr(self.__instance))
        print(self)
        return type.__new__(self, *args, **kwargs)
    
    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        super(singleton_meta, cls).__init__(name, bases, dct)
        
    def __call__(self, *args, **kwargs):
        print(repr(self.__instance))
        print(repr(self.xxx))
        if self not in self.__instance:
            self.__instance[self] = type.__call__(self, *args, **kwargs)
        return self.__instance[self]

'''
'metaclass = singleton_meta' -> this means the following: 
MyClass2 = singleton_meta('MyClass2', (object), dict(xxx = {}))
'''

class MyClass2(object, metaclass = singleton_meta):
    xxx = {}
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

if __name__ == '__main__':
    pt = Point(3, 4)
    print(repr(pt))
    print(pt.distance_from_origin())
    
    cr = Circle(5, 4, 3)
    print(repr(cr))
    print(cr.area())
    print(cr.circumference())
    print(cr.edge_distance_from_origin())
    
    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)
    s3 = MyClass()
    print(s3)
    print(s3.x)
    print(s3.y)
    s4 = MyClass()
    print(s4)
    print(s4.x)
    print(s4.distance_from_origin())
    
    s5 = MyClass2()
    print(s5)
    s6 = MyClass2()
    print(s6)
