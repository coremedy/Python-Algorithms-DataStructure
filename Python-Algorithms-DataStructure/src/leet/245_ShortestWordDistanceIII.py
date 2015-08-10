'''
Created on 2015-08-09
'''

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        distance = len(words)
        recorder = dict()
        for index in range(distance):
            if words[index] not in recorder:
                recorder[words[index]] = []
            recorder[words[index]].append(index)
        if word1 != word2:
            for i in recorder[word1]:
                for j in recorder[word2]:
                    distance = min(distance, max(i, j) - min(i, j))
        else:
            for i in range(0, len(recorder[word1]) - 1):
                for j in range(i + 1, len(recorder[word1])):
                    distance = min(distance, max(recorder[word1][i], recorder[word1][j]) - min(recorder[word1][i], recorder[word1][j]))
        return distance

if __name__ == '__main__':
    pass