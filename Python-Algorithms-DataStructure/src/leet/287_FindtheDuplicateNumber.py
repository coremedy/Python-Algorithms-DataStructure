'''
Created on 2015-10-20
the input is not ordered
but 1 - n is ordered
middle = (1 + n) / 2
if, in the array, there are more than 'middle' elements, this means dup appears on the right side of middle (pigeon-hole principle)
same for the left side
so, O(log(n)) for outer loop, O(n) for inner loop to make the count
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg, end = 1, len(nums) - 1
        while beg <= end:
            mid = (beg + end) // 2
            if sum([1 if n <= mid else 0 for n in nums]) > mid:
                end = mid - 1
            else:
                beg = mid + 1
        return beg

if __name__ == '__main__':
    pass