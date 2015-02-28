'''
Created on 2015-02-28

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=253
'''

import time
import bisect

if __name__ == '__main__':
    start_time = time.time()
    element_array = []
    # Get the input and sort
    with open('C:\\testcases\\algo1-programming_prob-2sum.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            element_array.append(int(line.strip()))
    element_array.sort()
    print('Processing input and sort --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    out = set()
    for x in element_array:
        # Binary search: index of element that is greater than -10000 - x
        lower = bisect.bisect_left(element_array, -10000 - x)
        # Binary search: index of element that is smaller than 10000 - x
        upper = bisect.bisect_right(element_array, 10000 - x)
        # This range of elements will get t within [-10000, 10000]
        # Use a set to eliminate duplicate t
        for y in element_array[lower:upper]:
            if (x != y) and (x + y not in out):
                out.add(x + y)
    print(len(out))
    print('Getting result --- %s seconds ---' % (time.time() - start_time))