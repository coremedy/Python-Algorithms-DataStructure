'''
Created on 2015-08-31
'''

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        same, index, i, j, result = (word1 == word2), 0, -1, -1, len(words)
        for w in words:
            if same and w == word1:
                i, j = j, index
            elif not same:
                i, j = index if w == word1 else i, index if w == word2 else j
            if i != -1 and j != -1:
                result = min(result, i - j if i - j > 0 else j - i)
            index += 1
        return result

if __name__ == '__main__':
    pass