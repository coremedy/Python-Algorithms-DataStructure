'''
Created on 2015-08-15
Extended version of Moore election
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        nums_len = len(nums)
        if nums_len < 3:
            return list(set(nums))
        candidate_1, count_1 = None, 0
        candidate_2, count_2 = None, 0
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = n
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = n
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        result = []
        if nums.count(candidate_1) > nums_len // 3:
            result.append(candidate_1)
        if nums.count(candidate_2) > nums_len // 3:
            result.append(candidate_2)        
        return result

if __name__ == '__main__':
    pass