'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

if __name__ == '__main__':
    '''
    set - mutable
    '''
    people = {"Buffy", "Angel", "Giles"}
    print(people)
    people.add("Willow")
    print(people)
    t = {"Tommy", }
    print(people | t)
    print(people.union(t))
    print(people & t)
    print(people.intersection(t))
    print(people - t)
    print(people.difference(t))
    '''
    change people here
    '''
    print(people.update(t))
    print(people)
    
    sunnydale = dict(name="Giles", age=45, hobby="Watch")
    print(sunnydale)
    
    sunnydale = dict([("name", "Willow"), ("age", 15), ("hobby", "nerding")])
    sunnydale
    
    '''
    Functional programming
    functions = dict(a=add_to_dict, e=edit_dict,...)
    functions[actions](db)
    '''
    