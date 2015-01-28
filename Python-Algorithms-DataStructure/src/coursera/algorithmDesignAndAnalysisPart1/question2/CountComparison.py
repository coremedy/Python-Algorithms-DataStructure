'''
Created on 2015-01-28

Question URL: https://class.coursera.org/algo-007/quiz/attempt?quiz_id=33
'''

def quick_sort(seq, book_mark, strategy):
    # Base case
    if len(seq) == 1:
        return seq
    elif len(seq) == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq
    # Then we need to find pivot
    else:
        if strategy == 2:
            # Use the last element of the array as the pivot element
            seq[0], seq[len(seq) - 1] = seq[len(seq) - 1], seq[0]
        elif strategy == 3:
            # Use "median-of-three" as the pivot element
            first_index = 0
            last_index = len(seq) - 1
            middle_index = last_index // 2
            min_val = min(seq[first_index], seq[middle_index], seq[last_index])
            max_val = max(seq[first_index], seq[middle_index], seq[last_index])
            # Assuming all elements are different
            if (min_val < seq[middle_index]) and (seq[middle_index] < max_val):
                seq[0], seq[middle_index] = seq[middle_index], seq[0]
            elif (min_val < seq[last_index]) and (seq[last_index] < max_val):
                seq[0], seq[last_index] = seq[last_index], seq[0]

        pivot = seq[0]
        ptr1 = 1
        for ptr2 in range(1, len(seq)):
            if seq[ptr2] <= pivot:
                if ptr2 != ptr1:
                    seq[ptr1], seq[ptr2] = seq[ptr2], seq[ptr1]
                # This ptr must move!
                if (ptr1 < len(seq) - 1):
                    ptr1 += 1
        # 'Recover' the pivot
        pivot_index = 0
        if seq[ptr1] <= pivot:
            seq[0], seq[ptr1] = seq[ptr1], seq[0]
            pivot_index = ptr1
        else:
            if (ptr1 - 1) >= 1:
                seq[0], seq[ptr1 - 1] = seq[ptr1 - 1], seq[0]
                pivot_index = ptr1 - 1
        # Divide
        if pivot_index == 0:
            book_mark['comparisons'] += len(seq) - 2
            return [pivot] + quick_sort(seq[pivot_index + 1:], book_mark, strategy)
        elif pivot_index == len(seq) - 1:
            book_mark['comparisons'] += len(seq) - 2
            return quick_sort(seq[:pivot_index], book_mark, strategy) + [pivot]
        else:
            book_mark['comparisons'] += len(seq) - 3
            return quick_sort(seq[:pivot_index], book_mark, strategy) + [pivot] + quick_sort(seq[pivot_index + 1:], book_mark, strategy)

if __name__ == '__main__':
    
    # Data structure for three strategies
    test_array_strategy1 = []
    test_array_strategy2 = []
    test_array_strategy3 = []
    
    book_mark_strategy1 = { 'comparisons' : 0 }
    book_mark_strategy2 = { 'comparisons' : 0 }
    book_mark_strategy3 = { 'comparisons' : 0 }

    # Get the input    
    with open('C:\\testcases\\QuickSort.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            test_array_strategy1.append(int(line.strip()))
            test_array_strategy2.append(int(line.strip()))
            test_array_strategy3.append(int(line.strip()))
    
    # Get the procedure going
    quick_sort(test_array_strategy1, book_mark_strategy1, 1)
    print(book_mark_strategy1['comparisons'] + len(test_array_strategy1) - 1)
    
    quick_sort(test_array_strategy2, book_mark_strategy2, 2)
    print(book_mark_strategy2['comparisons'] + len(test_array_strategy2) - 1)
    
    quick_sort(test_array_strategy3, book_mark_strategy3, 3)
    print(book_mark_strategy3['comparisons'] + len(test_array_strategy3) - 1)