'''
Created on 2015-08-11
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if len(nums) <= 1:
            return len(nums)
        max_len = [0]
        sets = []
        recorder = dict()
        for n in nums:
            if n not in recorder:
                if n - 1 not in recorder and n + 1 not in recorder:
                    sets.append([-1, 1])
                    max_len[0] = max(max_len[0], 1)
                    recorder[n] = len(sets) - 1
                elif n - 1 not in recorder and n + 1 in recorder:
                    recorder[n] = self.add_new_member(sets, recorder, n + 1, max_len)
                elif n - 1 in recorder and n + 1 not in recorder:
                    recorder[n] = self.add_new_member(sets, recorder, n - 1, max_len)
                else:
                    recorder[n] = self.merge_sets(sets, recorder, n - 1, n + 1, max_len)
        return max_len[0]
        
    def add_new_member(self, sets, recorder, k, max_len):
        current_index = recorder[k]
        while sets[current_index][0] != -1:
            current_index = sets[current_index][0]
        sets[current_index][1] += 1
        max_len[0] = max(max_len[0], sets[current_index][1])
        return current_index
        
    def merge_sets(self, sets, recorder, k, l, max_len):
        index_left = recorder[k]
        while sets[index_left][0] != -1:
            index_left = sets[index_left][0]        
        index_right = recorder[l]
        while sets[index_right][0] != -1:
            index_right = sets[index_right][0]
        if index_left == index_right:
            sets[index_left][1] += 1
            max_len[0] = max(max_len[0], sets[index_left][1])
            return index_left
        else:
            large_one = max(index_left, index_right)
            small_one = min(index_left, index_right)
            sets[small_one][1] += (sets[large_one][1] + 1)
            max_len[0] = max(max_len[0], sets[small_one][1])
            sets[large_one][1] = 0
            sets[large_one][0] = small_one
            return small_one

if __name__ == '__main__':
    pass