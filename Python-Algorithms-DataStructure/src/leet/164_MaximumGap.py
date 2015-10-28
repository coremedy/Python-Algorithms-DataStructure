'''
Created on 2015-10-28
Radix sort
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums_str, max_len = [], 0
        for n in nums:
            s = str(n)
            nums_str.append(s[::-1])
            max_len = max(max_len, len(s))
        for l in range(max_len):
            buckets = [[] for dummy_i in range(10)]
            for s in nums_str:
                if len(s) <= l:
                    buckets[0].append(s)
                else:
                    buckets[int(s[l])].append(s)
            nums_str = []
            for b in buckets:
                nums_str.extend(b)
        nums_result, gap = [int(s[::-1]) for s in nums_str], 0
        for index in range(1, len(nums_result)):
            gap = max(gap, nums_result[index] - nums_result[index - 1])
        return gap

if __name__ == '__main__':
    pass