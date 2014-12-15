'''
Created on 2014-12-15

Copyright info: code derived from http://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/
'''

from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from multiprocessing.dummy import Pool
from operator import itemgetter

def sanitize(w):
    # Strip from left
    while len(w) > 0 and not w[0].isalnum():
        w = w[1:]
    # Strip from right    
    while len(w) > 0 and not w[-1].isalnum():
        w = w[:-1]       
    return w  

'''
receiving a list of words
returning [('Title1' , 1), ('Title2', 1), ...]
'''
def map_worker(L):
    result = []
    
    for w in L:
        if not w.isalnum():
            w = sanitize(w)
        if w.istitle():
            result.append((w, 1))
    
    return result

'''
receiving [[('Title1' , 1), ('Title2', 1), ...], ...]
returning {'Title1' : [('Title1' , 1), ...], 'Title2' : [('Title2' , 1), ...], ... }
'''
def partition_worker(L):
    tf = {}
    
    for sublist in L:
        for p in sublist:
            if p[0] not in tf:
                tf[p[0]] = []
            tf[p[0]].append(p)
    
    return tf

'''
receiving ('Title1', [('Title1' , 1), ...]), coming from tf.items()
returning ('Title1', result)
'''
def reduce_worker(tup):
    return (tup[0], sum(p[1] for p in tup[1]))

def load_file(path):
    word_list = []
    with open(path, "r") as file:
        for line in file:
            word_list.append(line)
    # Efficiently concatenate Python string objects
    return (' '.join(word_list)).split()

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

if __name__ == '__main__':
    text = load_file('C:\\test.txt')
    
    # Build a pool of 8 processes
    pool = Pool(processes=8,)
    
    # Fragment the string data into 8 chunks
    partitioned_text = list(chunks(text, int(len(text) / 8)))
    
    # Generate count tuples for title-cased tokens
    single_count_tuples = pool.map(map_worker, partitioned_text)
    
    # Organize the count tuples; lists of tuples by token key
    token_to_tuples = partition_worker(single_count_tuples)
    
    # Collapse the lists of tuples into total term frequencies
    term_frequencies = pool.map(reduce_worker, token_to_tuples.items())
    
    # Result
    # https://docs.python.org/3/howto/sorting.html
    print(sorted(term_frequencies, key = itemgetter(1,0)))