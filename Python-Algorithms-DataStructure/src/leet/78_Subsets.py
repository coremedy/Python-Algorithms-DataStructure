'''
Created on 2015-07-26
This also covers 90 Subsets II
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[], nums]
        else:
            nums.sort()
            result_dict = dict()
            result = []
            for n in range(1 << len(nums)):
                temp_result = []
                for bit_index in range(len(nums) - 1, -1, -1):
                    if ((1 << bit_index) & (n)) > 0:
                        temp_result.append(nums[len(nums) - 1 - bit_index])
                temp_tup = tuple(temp_result)                  
                if temp_tup not in result_dict:
                    result_dict[temp_tup] = True
                    result.append(temp_result)
            return result

if __name__ == '__main__':
    pass