'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

class SimpleTree(object):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children and children or []
    
    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value)+ "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

if __name__ == '__main__':
    st = SimpleTree('a', [SimpleTree('b', [SimpleTree('d'),
                                           SimpleTree('e')] ), SimpleTree('c', [SimpleTree('h'),
                                                                                SimpleTree('g')]) ])
    print(st)