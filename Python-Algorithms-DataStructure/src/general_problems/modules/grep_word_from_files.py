'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def grep_word_from_files(filename, word):
    with open(filename) as file:
        for lino, line in enumerate(file, start = 1):
            if word in line:
                print("{0}:{1}:{2:.40}".format(filename, lino, line.rstrip()))

if __name__ == '__main__':
    grep_word_from_files("C:\\test.txt", "instance")