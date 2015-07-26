'''
Created on 2015-07-26
'''

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.BackTrack(candidates, target, 0, result, [])
        return result
        
    def BackTrack(self, candidates, target, start, result, cache):
        if target == 0:
            result.append(list(cache))
        elif target > 0:
            index = start
            while index < len(candidates):
                cache.append(candidates[index])
                self.BackTrack(candidates, target - candidates[index], index + 1, result, cache)
                value = cache.pop()
                index += 1
                # Pruning
                while index < len(candidates) and candidates[index] == value:
                    index += 1

if __name__ == '__main__':
    pass