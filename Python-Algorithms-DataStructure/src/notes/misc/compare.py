'''
2015-10-24
'''

import sys
import os

def openFile(path, mode):
    fh = None
    try:
        fh = open(path, mode)
    except IOError:
        print("Error: path " + path + " is invalid!")
        print("Usage: python compare.py file1_path file2_path output_file_path")
    return fh

def closeFiles(fileHandler1, fileHandler2, outputFileHandler, outputFilePath, remove):
    if fileHandler1:
        fileHandler1.close()
    if fileHandler2:
        fileHandler2.close()
    if outputFileHandler:
        outputFileHandler.close()
        if remove:
            os.remove(outputFilePath)    

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python compare.py file1_path file2_path output_file_path")
        exit(1)
    # Open File
    fileHandler1, fileHandler2, outputFileHandler = openFile(sys.argv[1], 'r'), openFile(sys.argv[2], 'r'), openFile(sys.argv[3], 'w+')
    if not fileHandler1 or not fileHandler2 or not outputFileHandler:
        closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
        exit(1)
    # Process the first one
    d = dict()
    for line in fileHandler1:
        tok = line.strip().split()
        if len(tok) != 2:
            print('Error: ' + sys.argv[1] + ' has Invalid format!')
            closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
            exit(1)
        if tok[0] not in d:
            d[tok[0]] = tok[1]
        else:
            print('Error: ' + sys.argv[1] + ' has duplicate host name!')
            closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
            exit(1)
    if not d:
        print('Error: ' + sys.argv[1] + ' is empty!')
        closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
        exit(1)
    # Process the second one
    result, max_len = [], -1
    for line in fileHandler2:
        tok = line.strip().split()
        if len(tok) != 2:
            print('Error: ' + sys.argv[2] + ' has Invalid format!')
            closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
            exit(1)
        underscore_pos = tok[0].find('_')
        key = tok[0][:underscore_pos if underscore_pos != -1 else len(tok[0])]
        if key in d:
            if d[key] != tok[1]:
                result.append([key, d[key], tok[0], tok[1]])
                max_len = max(max_len, max([len(s) for s in result[-1]]))
        else:
            result.append(['[None]', '[None]', tok[0], tok[1]])
            max_len = max(max_len, max([len(s) for s in result[-1]]))
    if not result:
        print('Error: ' + sys.argv[1] + ' is empty!')
        closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], True)
        exit(1)
    # Output
    outputFileHandler.write('KEY IN FILE1'.ljust(max_len + 1) + 'VAL IN FILE1'.ljust(max_len + 1) + 'KEY IN FILE2'.ljust(max_len + 1) + 'VAL IN FILE2'.ljust(max_len + 1) + '\n')  
    for row in result:
        outputFileHandler.write(''.join([s.ljust(max_len + 1) for s in row]) + '\n')
    # Done
    closeFiles(fileHandler1, fileHandler2, outputFileHandler, sys.argv[3], False)
