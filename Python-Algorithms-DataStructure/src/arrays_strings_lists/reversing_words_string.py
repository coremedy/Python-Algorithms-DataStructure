'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def reversing_words_in_sentence(sentence):
    '''
    This illustrates how we should write the function in a Python way ....
    split - splitting string with space
    reversed - reverse the list and return iterator
    join - call the iterator and join all elements of a list, separated by ' '
    '''
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    sentence = 'Autobots, move on!'
    print(reversing_words_in_sentence(sentence))