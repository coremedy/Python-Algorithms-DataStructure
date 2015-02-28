'''
Created on 2015-02-28

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=253
'''

import time
import heapq

if __name__ == '__main__':
    start_time = time.time()
    # max heap
    low_heap = []
    # min heap
    high_heap = []
    # Get the input and sort
    count = 0
    result = 0
    with open('C:\\testcases\\Median.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            elem = int(line.strip())
            # Insert into either one
            if len(high_heap) == 0:
                heapq.heappush(high_heap, elem)
            else:
                if elem > high_heap[0]:
                    heapq.heappush(high_heap, elem)
                else:
                    if len(low_heap) == 0:
                        heapq.heappush(low_heap, -elem)
                    else:
                        if elem < -low_heap[0]:
                            heapq.heappush(low_heap, -elem)
                        else:
                            heapq.heappush(high_heap, elem)
            count += 1
            # Balance the heap
            # Even
            size_of_high_heap = 0
            if count % 2 == 0:
                size_of_high_heap = count // 2
                while len(high_heap) > size_of_high_heap:
                    heapq.heappush(low_heap, -heapq.heappop(high_heap))
                while len(high_heap) < size_of_high_heap:
                    heapq.heappush(high_heap, -heapq.heappop(low_heap))
                result += -low_heap[0]
            # Odd
            else:
                size_of_high_heap = (count // 2) + 1
                while len(high_heap) > size_of_high_heap:
                    heapq.heappush(low_heap, -heapq.heappop(high_heap))
                while len(high_heap) < size_of_high_heap:
                    heapq.heappush(high_heap, -heapq.heappop(low_heap))               
                result += high_heap[0]
    print(result % 10000)
    print('Getting result --- %s seconds ---' % (time.time() - start_time))