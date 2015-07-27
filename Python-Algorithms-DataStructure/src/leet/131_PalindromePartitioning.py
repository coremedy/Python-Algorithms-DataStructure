'''
Created on 2015-07-27
'''

class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        table = dict()
        table[''] = True
        s_length = len(s)
        for index in range(s_length):
            if s[index] not in table:
                table[s[index]] = True
        for row in range(s_length, -1, -1):
            for col in range(row + 1, s_length):
                if s[row : col + 1] not in table:
                    table[s[row : col + 1]] = (s[row] == s[col]) and table[s[row + 1: col]]
        result = []
        self.BackTrack(s, table, result, [])
        return result
        
    def BackTrack(self, s, table, result, cache):
        if len(s) == 0:
            result.append(cache)
            return
        for index in range(len(s), 0, -1):
            if table[s[:index]]:
                self.BackTrack(s[index:], table, result, cache + [s[:index]])

if __name__ == '__main__':
    pass