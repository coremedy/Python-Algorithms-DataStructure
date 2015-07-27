'''
Created on 2015-07-27
'''

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        s_length = len(s)
        if s_length < 4 or s_length > 12:
            return []
        result = []
        self.BackTrack(s, 0, result, [])
        return result
        
    def BackTrack(self, s, depth, result, cache):
        if len(s) == 0 and depth == 4:
            result.append('.'.join(cache))
            return
        if len(s) == 0:
            return
        if depth == 4:
            return
        for index in range(0, min(3, len(s))):
            if index == 2 and int(s[0:3]) > 255:
                break
            self.BackTrack(s[index + 1:], depth + 1, result, cache + [s[:index + 1]])
            if index == 0 and int(s[0]) == 0:
                break

if __name__ == '__main__':
    pass