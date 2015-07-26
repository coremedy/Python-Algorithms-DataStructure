'''
Created on 2015-07-26
Use recursion to control loop (you will need k loop if you use the iteration method ... which is hard to code)
'''

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k == 0:
            return []
        if k >= n:
            return [[i for i in range(1, n + 1)]]
        result = []
        self.backTrack(1, n, k, 0, result, [])
        return result
        
    def backTrack(self, s, n, k, depth, result, cache):
        # Baseline
        if depth == k:
            result.append(list(cache))         
        else:
            for i in range(s, n + 1):
                cache.append(i)
                self.backTrack(i + 1, n, k, depth + 1, result, cache)
                cache.pop()                                 
   
if __name__ == '__main__':
    pass