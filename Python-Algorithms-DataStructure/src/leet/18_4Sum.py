'''
Created on 2015-08-15
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        recorder = dict()
        for outer_index in range(len(nums) - 1):
            for inner_index in range(outer_index + 1, len(nums)):
                val = nums[outer_index] + nums[inner_index]
                if val not in recorder:
                    recorder[val] = []
                recorder[val].append((outer_index, inner_index))
        inter_result = set()
        for outer_index in range(len(nums) - 3):
            for inner_index in range(outer_index + 1, len(nums) - 2):
                if target - nums[outer_index] - nums[inner_index] in recorder:
                    for tup in recorder[target - nums[outer_index] - nums[inner_index]]:
                        if tup[0] > inner_index:
                            inter_result.add((nums[outer_index], nums[inner_index], nums[tup[0]], nums[tup[1]]))
        return [list(t) for t in inter_result]
    
    def fourSum_TLE(self, nums, target):
        result = []
        if len(nums) < 4:
            return result
        nums.sort()
        index_first = 0  
        while index_first < len(nums) - 3:
            index_second = index_first + 1
            while index_second < len(nums) - 2:
                current_target = target - nums[index_first] - nums[index_second]
                index_third = index_second + 1
                index_fourth = len(nums) - 1
                while index_third < index_fourth:
                    if current_target == nums[index_third] + nums[index_fourth]:
                        result.append([nums[index_first], nums[index_second], nums[index_third], nums[index_fourth]])
                    if current_target <= nums[index_third] + nums[index_fourth]:
                        index_third += 1
                        while index_third < index_fourth and nums[index_third] == nums[index_third - 1]:
                            index_third += 1
                    if current_target >= nums[index_third] + nums[index_fourth]:
                        index_fourth -= 1
                        while index_third < index_fourth and nums[index_fourth] == nums[index_fourth + 1]:
                            index_fourth -= 1
                index_second += 1
                while index_second < len(nums) - 2 and nums[index_second] == nums[index_second - 1]:
                    index_second += 1
            index_first += 1
            while index_first < len(nums) - 3 and nums[index_first] == nums[index_first - 1]:
                index_first += 1
        return result

if __name__ == '__main__':
    pass