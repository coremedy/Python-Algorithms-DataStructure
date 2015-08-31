'''
Created on 2015-08-31
'''

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        i, j, index, result = -1, -1, 0, len(words)
        for w in words:
            if w == word1:
                i = index
            if w == word2:
                j = index
            if i != -1 and j != -1:
                result = min(result, max(i, j) - min(i, j))
            index += 1
        return result

if __name__ == '__main__':
    pass