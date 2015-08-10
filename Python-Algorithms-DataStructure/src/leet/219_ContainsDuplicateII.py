'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        recorder = dict()
        for index in range(len(nums)):
            if nums[index] not in recorder:
                recorder[nums[index]] = index
            else:
                if index - recorder[nums[index]] <= k:
                    return True
                # No need to record all indices. Latest is closest.
                recorder[nums[index]] = index
        return False
 

if __name__ == '__main__':
    pass