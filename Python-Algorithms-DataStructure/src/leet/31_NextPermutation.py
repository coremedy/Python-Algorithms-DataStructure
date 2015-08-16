'''
Created on 2015-08-16
'''

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) > 1:
            # The pattern of the sequence should be first increase and then decrease
            # Find the peak point and then swap peak - 1 with suitable element in (peak, len(nums) - 1)
            # Finally reverse (peak, len(nums) - 1)
            # If the peak is 0, reverse the entire sequence
            prev = len(nums) - 1
            for index in range(len(nums) - 2, -1, -1):
                if nums[index] < nums[prev]:
                    break
                prev = index
            candidate = prev - 1
            # Determine the candidate to move
            if candidate != -1:
                for index in range(len(nums) - 1, candidate, -1):
                    if nums[index] > nums[candidate]:
                        nums[index], nums[candidate] = nums[candidate], nums[index]
                        break
            begin = prev
            end = len(nums) - 1
            # Reverse
            while begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1

if __name__ == '__main__':
    pass