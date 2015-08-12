'''
Created on 2015-08-11
'''

class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, numbers, target):
        begin = 0
        end = len(numbers) - 1
        while begin != end:
            if numbers[begin] + numbers[end] == target:
                return [begin + 1, end + 1]
            elif numbers[begin] + numbers[end] > target:
                end -= 1
            else:
                begin += 1
        return []

if __name__ == '__main__':
    pass