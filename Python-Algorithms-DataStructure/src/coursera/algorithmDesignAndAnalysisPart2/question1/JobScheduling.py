'''
Created on 2015-03-24

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=75
'''

import time

class schedule_difference(object):
    
    def __init__(self, weight, length):
        self._weight = weight
        self._length = length
    
    def __lt__(self, other):
        if (self._weight - self._length) > (other._weight - other._length):
            return True
        elif (self._weight - self._length) == (other._weight - other._length):
            return (self._weight > other._weight)
        else:
            return False
        
class schedule_ratio(object):
    
    def __init__(self, weight, length):
        self._weight = weight
        self._length = length
    
    def __lt__(self, other):
        return ((float(self._weight) / float(self._length)) > (float(other._weight) / float(other._length)))

if __name__ == '__main__':
    start_time = time.time()
    task_array_difference = []
    task_array_ratio = []
    number_of_tasks = 0
    # Read input
    with open('C:\\testcases\\jobs.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 1:
                number_of_tasks = int(data[0])
            else:
                task_array_difference.append(schedule_difference(int(data[0]), int(data[1])))
                task_array_ratio.append(schedule_ratio(int(data[0]), int(data[1])))
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    # Sort - O(nlogn)
    start_time = time.time()           
    sorted_task_array_difference = sorted(task_array_difference)
    sorted_task_array_ratio = sorted(task_array_ratio)
    print('Sorting --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    timeline_difference = 0
    result_difference = 0
    timeline_ratio = 0
    result_ratio = 0
    for index in range(0, number_of_tasks):
        timeline_difference += sorted_task_array_difference[index]._length
        timeline_ratio += sorted_task_array_ratio[index]._length
        result_difference += sorted_task_array_difference[index]._weight * timeline_difference
        result_ratio += sorted_task_array_ratio[index]._weight * timeline_ratio
    print('Final calculation --- %s seconds ---' % (time.time() - start_time))
    print(result_ratio, result_difference)