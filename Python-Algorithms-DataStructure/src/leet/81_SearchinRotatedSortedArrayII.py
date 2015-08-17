'''
Created on 2015-08-17
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True if nums[0] == target else False
        # Search for rotation point
        begin = 0
        end = len(nums) - 1
        # Note the difference with ordinary binary sort
        # Difference 1
        while end - begin > 1:
            # Difference 2
            while begin + 1 < end and nums[begin] == nums[begin + 1]:
                begin += 1
            if end - begin == 1:
                break
            while end - 1 > begin and nums[end] == nums[end - 1]:
                end -= 1            
            if end - begin == 1:
                break
            # Then here is the normal procedure
            # The invariant is interesting
            # begin will move to the largest val
            # end will move to the smallest val
            mid = (begin + end) // 2
            if nums[begin] <= nums[mid]:
                begin = mid
            else:
                end = mid
        if end == 0:
            return self.binary_search(nums, 0, len(nums) - 1, target)
        if target >= nums[end] and target <= nums[-1]:
            return self.binary_search(nums, end, len(nums) - 1, target)
        if target >= nums[0] and target <= nums[end - 1]:
            return self.binary_search(nums, 0, end - 1, target)
        return False

    def binary_search(self, nums, begin, end, target):
        while begin != end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            else:
                begin = mid + 1
        if nums[begin] == target:
            return True
        else:
            return False

if __name__ == '__main__':
    pass