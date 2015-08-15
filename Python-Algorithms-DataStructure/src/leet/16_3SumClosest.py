'''
Created on 2015-08-15
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        result = None
        # Rule-out base cases
        nums_len = len(nums)
        if nums_len < 3:
            return result
        # Then real procedure
        nums.sort()
        # We need three element
        index_first = 0
        result = nums[index_first] + nums[index_first + 1] + nums[nums_len - 1]
        while index_first < nums_len - 2:
            current_target = target - nums[index_first]
            # Similar as Two Sum II - Input array is sorted
            index_second = index_first + 1
            index_third = nums_len - 1
            while index_second < index_third:
                temp_target = nums[index_second] + nums[index_third]
                if temp_target == current_target:
                    return target
                if abs(temp_target + nums[index_first] - target) < abs(result - target):
                    result = temp_target + nums[index_first]
                if temp_target > current_target:
                    index_third -= 1
                    while index_third > index_second and nums[index_third] == nums[index_third + 1]:
                        index_third -= 1
                if temp_target < current_target:
                    index_second += 1
                    while index_second < index_third and nums[index_second] == nums[index_second - 1]:
                        index_second += 1
            index_first += 1
            while index_first <= nums_len - 2 and nums[index_first] == nums[index_first - 1]:
                index_first += 1
        return result

if __name__ == '__main__':
    pass