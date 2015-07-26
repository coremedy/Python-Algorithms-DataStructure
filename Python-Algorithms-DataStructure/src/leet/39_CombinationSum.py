'''
Created on 2015-07-26
'''

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        self.backTrack(candidates, target, 0, result, [])
        return result
    
    def backTrack(self, candidates, target, start, result, cache):
        if target == 0:
            result.append(list(cache))
        elif target > 0:
            # Do pruning here!
            # [2,3,6,7], 7
            # If 2, 2, 3 is covered in the subtree originated from 2
            # When we reach the subtrees of 3, we don't need to consider 2
            # This will help to eliminate dup and unnecessary calculation
            for index in range(start, len(candidates)):
                cache.append(candidates[index])
                self.backTrack(candidates, target - candidates[index], index, result, cache)
                cache.pop()   

if __name__ == '__main__':
    pass