'''
Created on 2015-08-09
Another method:
reverse(nums, 0, n - k - 1)
reverse(nums, n - k, n - 1)
reverse(nums, 0, n - 1)
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if nums is None:
            return
        nums_length = len(nums)
        if nums_length == 0:
            return
        k = k % nums_length
        if k == 0:
            return
        curr_index = 0
        curr_val = nums[0]
        distance = 0
        for dummy_i in range(nums_length):
            next_index = (curr_index + k) % nums_length
            next_val = nums[next_index]
            nums[next_index] = curr_val
            curr_val = next_val
            curr_index = next_index
            # Cycle detection and move the index by 1
            distance = (distance + k) % nums_length
            if distance == 0:
                curr_index = (curr_index + 1) % nums_length
                curr_val = nums[curr_index]
        return

if __name__ == '__main__':
    pass