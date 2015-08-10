'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        # Backward
        nums1_index, nums2_index, overall_index = m - 1, n - 1, m + n - 1
        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[overall_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[overall_index] = nums2[nums2_index]
                nums2_index -= 1
            overall_index -= 1
        while nums2_index >= 0:
            nums1[overall_index] = nums2[nums2_index]
            overall_index -= 1
            nums2_index -= 1
  
        

if __name__ == '__main__':
    pass