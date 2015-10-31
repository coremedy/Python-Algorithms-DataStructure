'''
Created on 2015-10-31
Pass 1: get the xor of a and b
Then find the first different bit using r & (-r)
Pass 2: decide a and b according to different bit
http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r, a, b = 0, 0, 0
        for n in nums:
            r ^= n
        r = r & (-r)
        for n in nums:
            if n & r == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]

if __name__ == '__main__':
    pass