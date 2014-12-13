'''
Created on 2014-12-13

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''
import string

def count_unique_word(file_name):
    words = dict()
    strip = string.whitespace + string.punctuation + string.digits + '\'"`'
    with open(file_name) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1
    for word in sorted(words.keys()):
        print('{0} occurred {1} times'.format(word, words[word]))

if __name__ == '__main__':
    count_unique_word('C:\\test.txt')