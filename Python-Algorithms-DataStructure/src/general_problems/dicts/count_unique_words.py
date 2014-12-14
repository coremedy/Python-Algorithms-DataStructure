'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

import collections
import string
def count_unique_word(file_name):
    words = collections.defaultdict(int)
    strip = string.whitespace + string.punctuation + string.digits + "\"'`"
    with open(file_name) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
    for word in sorted(words):
        print("'{0}' occurs {1} times.".format(word, words[word]))

if __name__ == '__main__':
    count_unique_word("C:\\test.txt")