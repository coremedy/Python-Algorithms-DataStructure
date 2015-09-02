'''
Created on 2015-09-02
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Quite interesting solution
        # Get all raw ones
        hash_sum, words_set, word_len, words_len = sum([hash(w) for w in words]), set(words), len(words[0]), len(words)
        hash_array = [hash(s[i : i + word_len]) if s[i : i + word_len] in words_set else 0 for i in range(len(s) - word_len + 1)]
        raw_result = [i for i in range(len(s) - words_len * word_len + 1) if sum(hash_array[i : i + words_len * word_len : word_len]) == hash_sum]
        # Kick out the wrong ones
        if len(raw_result) > 0:
            d = dict()
            for w in words:
                if w not in d:
                    d[w] = 0
                d[w] += 1
            result = []
            for index in raw_result:
                d_temp, correct = dict(), True
                for beg in range(index, index + words_len * word_len, word_len):
                    w = s[beg : beg + word_len]
                    if w not in d_temp:
                        d_temp[w] = 0
                    d_temp[w] += 1
                    if d_temp[w] > d[w]:
                        correct = False
                        break
                if correct:
                    result.append(index)
            return result
        else:
            return raw_result

if __name__ == '__main__':
    pass