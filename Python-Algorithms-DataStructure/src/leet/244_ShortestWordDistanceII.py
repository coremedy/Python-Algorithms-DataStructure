'''
Created on 2015-08-31
'''

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d, self.cache, self.len, index = {}, {}, len(words), 0
        for w in words:
            if w in self.d:
                self.d[w].append(index)
            else:
                self.d[w] = [index]
            index += 1

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]
        if (word2, word1) in self.cache:
            return self.cache[(word2, word1)]
        m, n, m_index, n_index, result = self.d[word1], self.d[word2], 0, 0, self.len
        while m_index < len(m) and n_index < len(n):
            result, m_index, n_index = min(result, (n[n_index] - m[m_index]) if m[m_index] < n[n_index] else (m[m_index] - n[n_index])), m_index + 1 if m[m_index] < n[n_index] else m_index, n_index if m[m_index] < n[n_index] else n_index + 1
        self.cache[(word1, word2)], self.cache[(word2, word1)] = result, result
        return result

if __name__ == '__main__':
    pass