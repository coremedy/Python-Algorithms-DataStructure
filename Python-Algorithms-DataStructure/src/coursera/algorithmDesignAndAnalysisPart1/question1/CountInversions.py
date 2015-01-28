'''
Created on 2015-01-21

Question URL: https://class.coursera.org/algo-007/quiz?quiz_type=homework
'''

def merge_and_count(array, book_mark):
    # Base cases
    if len(array) == 1:
        # No need to touch book_mark
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            book_mark['inversions'] += 1
            array[0], array[1] = array[1], array[0]
        return array
    # Common cases
    else:
        mid = (len(array) - 1) // 2 + 1
        left = merge_and_count(array[:mid], book_mark)
        right = merge_and_count(array[mid:], book_mark)
        # Okay, take care here
        result = []
        while left and right:
            # Inversions!
            if left[-1] > right[-1]:
                book_mark['inversions'] += len(right)
                result.append(left.pop())
            # The rest
            else:
                result.append(right.pop())
        result.reverse()
        return (left or right) + result

if __name__ == '__main__':
    # Get the input first
    test_array = []
    with open('C:\\testcases\\IntegerArray.txt', 'r') as input_fileHandle:
        for line in input_fileHandle:
            test_array.append(int(line.strip()))
    book_mark = { 'inversions' : 0 }
    # Do the job
    merge_and_count(test_array, book_mark)
    print(book_mark['inversions'])