'''
Created on 2015-02-15

https://class.coursera.org/principlescomputing1-002/assignment
'''

"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    if line is None:
        return []
    if len(line) < 2:
        return line
    # valid input
    result_list = [0 for dummy_index in range(0, len(line))]
    merged = False
    last_elem_index = -1
    for index in range(0, len(line)):
        # bypass zero
        if line[index] == 0:
            continue
        else:
            # valid merge situation
            if (result_list[last_elem_index] == line[index]) and (merged == False):
                result_list[last_elem_index] += line[index]
                merged = True
            else:
                last_elem_index += 1
                result_list[last_elem_index] = line[index]
                if merged == True:
                    merged = False
    return result_list

if __name__ == '__main__':
    pass