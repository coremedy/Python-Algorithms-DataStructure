'''
Created on 2014-12-23

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

class BunchClass(dict):
    def __init__(self, *args, **kwds):
        super(BunchClass, self).__init__(*args, **kwds)
        self.__dict__ = self

if __name__ == '__main__':
    bc = BunchClass # notice the absence of ()
    tree = bc(left = bc(left="Buffy", right="Angel"), right = bc(left="Willow", right="Xander"))
    print(tree)