'''
Created on 2015-08-09
'''

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        distance = len(words)
        recorder = dict()
        for index in range(distance):
            if words[index] not in recorder:
                recorder[words[index]] = []
            recorder[words[index]].append(index)
        for i in recorder[word1]:
            for j in recorder[word2]:
                distance = min(distance, max(i, j) - min(i, j))
        return distance

if __name__ == '__main__':
    pass