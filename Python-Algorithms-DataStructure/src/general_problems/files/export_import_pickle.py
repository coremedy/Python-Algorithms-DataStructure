'''
Created on 2014-12-15

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import pickle
import os
import sys
import gzip

def export_pickle(data, filename='C:\\test.dat', compress=False):
    fh = None
    try:
        if compress:
            fh = gzip.open(filename, 'wb')
        else:
            fh = open(filename, 'wb')
        pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
    except (EnvironmentError, pickle.PicklingError) as err:
        print("{0}: export error: {1}".format(os.path.basename(sys.argv[0], err)))
    finally:
        if fh is not None:
            fh.close()

def import_pickle(filename):
    fh = None
    try:
        fh = open(filename, 'rb')
        return pickle.load(fh)
    except (EnvironmentError) as err:
        print ("{0}: import error: {1}".format(os.path.basename(sys.argv[0]), err))
        return False
    finally:
        if fh is not None:
            fh.close()

if __name__ == '__main__':
    mydict = {'a': 1, 'b': 2, 'c': 3}
    print(mydict)
    export_pickle(mydict)
    mydict2 = import_pickle('C:\\test.dat')
    print(mydict2)   