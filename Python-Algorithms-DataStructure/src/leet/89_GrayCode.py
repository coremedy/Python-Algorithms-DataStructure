'''
Created on 2015-07-26
'''

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return self.backTrack(0, n, [0], set([0]), [False])
    
    def backTrack(self, current, n, result_array, result_set, stop_flag):
        # Baseline
        if (1 << n) == len(result_array):
            stop_flag[0] = True
            return result_array
        # Back tracking
        for bit_index in range(n):
            target_bit = (1 << bit_index) & current
            next_candidate = (current | (1 << bit_index)) if not target_bit else (current & (~target_bit))
            if self.countDifferentBits(current, next_candidate) == 1 and next_candidate not in result_set:
                result_array.append(next_candidate)
                result_set.add(next_candidate)
                self.backTrack(next_candidate, n, result_array, result_set, stop_flag)
                if stop_flag[0]:
                    return result_array
                result_array.pop()
                result_set.remove(next_candidate)
    
    def countDifferentBits(self, a, b):
        c = a ^ b
        count = 0
        while c > 0:
            if (1 & c) == 1:
                count += 1
            c = c >> 1
        return count

if __name__ == '__main__':
    pass