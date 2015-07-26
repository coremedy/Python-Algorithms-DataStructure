'''
Created on 2015-07-26
'''

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        self.BackTrack(1, 0, k, n, result, [])
        return result
    
    def BackTrack(self, start, depth, k, n, result, cache):
        if depth == k:
            if n == 0:
                result.append(list(cache))
        else:
            for elem in range(start, 10):
                cache.append(elem)
                self.BackTrack(elem + 1, depth + 1, k, n - elem, result, cache)
                cache.pop()

if __name__ == '__main__':
    pass