'''
Created on 2015-01-31
Moore voting algorithm
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for n in nums:
            if candidate is None:
                candidate = n
                count = 1
            else:
                if candidate == n:
                    count += 1
                else:
                    if count == 0:
                        candidate = n
                        count = 1
                    else:
                        count -= 1
        return candidate
        # the majority element always exists so we skip the following check 
        #count = 0
        #for n in nums:
        #    if n == candidate:
        #        count += 1
        #if count > (len(nums) // 2):
        #    return candidate
        #return -1

if __name__ == '__main__':
    pass