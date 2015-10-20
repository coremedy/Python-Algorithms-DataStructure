'''
Created on 2015-10-20
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        beg, end = 0, len(nums) - 1
        while True:
            pivot = self.partition(nums, beg, end, (beg + end) // 2)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot > k - 1:
                end = pivot - 1
            else:
                beg = pivot + 1
        
    def partition(self, nums, beg, end, pivot):
        if beg == end:
            return beg
        pivot_value, nums[pivot], nums[end], start = nums[pivot], nums[end], nums[pivot], beg
        for index in range(beg, end):
            if nums[index] > pivot_value:
                nums[index], nums[start] = nums[start], nums[index]
                start += 1
        nums[start], nums[end] = nums[end], nums[start]
        return start

if __name__ == '__main__':
    pass