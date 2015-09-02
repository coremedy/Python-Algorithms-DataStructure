'''
Created on 2015-09-02
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d, count = dict(), len(t)
        for ch in t:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        beg, min_beg, index, result_len = 0, 0, 0, len(s) + 1
        for ch in s:
            if ch in d:
                d[ch], count = d[ch] - 1, count - 1 if d[ch] > 0 else count
            if count == 0:
                while True:
                    if s[beg] in d:
                        if d[s[beg]] < 0:
                            d[s[beg]] += 1
                        else:
                            break
                    beg += 1
                if index - beg + 1 <= result_len:
                    result_len = index - beg + 1
                    min_beg = beg
            index += 1
        return '' if result_len == len(s) + 1 else s[min_beg:min_beg + result_len]

if __name__ == '__main__':
    pass