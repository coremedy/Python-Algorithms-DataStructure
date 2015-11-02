'''
Created on 2015-11-02
'''

import collections

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        d = collections.OrderedDict()
        for index in range(len(nums)):
            x = nums[index] // max(1, t)
            # Don't worry about dup
            # If there is dup within valid range k, we should return True here!
            # That's why the 'window' invariant is valid here
            for c in [x - 1, x, x + 1]:
                if c in d and abs(d[c] -  nums[index]) <= t:
                    return True
            d[x] = nums[index]
            if index >= k:
                d.popitem(last=False)
        return False

if __name__ == '__main__':
    pass