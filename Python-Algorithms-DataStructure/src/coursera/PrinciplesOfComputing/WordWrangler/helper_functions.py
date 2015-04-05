'''
Created on 2015-04-05

https://class.coursera.org/principlescomputing2-002/assignment/view?assignment_id=13
'''

"""
Student code for Word Wrangler game
"""

import poc_wrangler_provided as provided # @UnresolvedImport
 
WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) <= 1:
        return list1
    else:
        filter_dict = dict()
        answer = []
        for member in list1:
            if member not in filter_dict:
                answer.append(member)
                filter_dict[member] = True
        return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    filter_dict = dict()
    for member in list1:
        filter_dict[member] = True
    answer = []
    for member in list2:
        if member in filter_dict:
            answer.append(member)
    return answer

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    answer = []
    list1_index = 0
    list2_index = 0
    
    while (list1_index < len(list1)) and (list2_index < len(list2)):
        if list1[list1_index] < list2[list2_index]:
            answer.append(list1[list1_index])
            list1_index += 1
        elif list1[list1_index] > list2[list2_index]:
            answer.append(list2[list2_index])
            list2_index += 1
        else:
            answer.append(list1[list1_index])
            answer.append(list2[list2_index])
            list1_index += 1
            list2_index += 1
            
    while list1_index < len(list1):
        answer.append(list1[list1_index])
        list1_index += 1
    while list2_index < len(list2):
        answer.append(list2[list2_index])
        list2_index += 1

    return answer
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    
    if len(list1) <= 1:
        return list1
    
    if len(list1) == 2:
        return [min(list1), max(list1)]
    
    mid = len(list1) / 2
    
    return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
    if len(word) == 0:
        return [""]
    
    first_character = word[0:1]
    intermediate_list = gen_all_strings(word[1:])
    answer = list(intermediate_list)
    
    for single_str in intermediate_list:
        if len(single_str) == 0:
            answer.append(first_character)
        else:
            for index_char in range(0, len(single_str) + 1):
                answer.append(single_str[0:index_char] + first_character + single_str[index_char:])

    return answer

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

if __name__ == '__main__':
    pass