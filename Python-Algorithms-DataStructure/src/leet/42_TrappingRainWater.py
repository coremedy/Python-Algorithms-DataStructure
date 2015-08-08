'''
Created on 2015-08-07
Something like 'Best time to buy and sell stock'
Scan from left for max and Scan from right for max
Then fetch the min and get the amount
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0
        if len(height) == 0:
            return 0
        length = len(height)
        left_max_val = height[0]
        left_max = [left_max_val for dummy_index in range(length)]
        right_max_val = height[-1]
        right_max = [right_max_val for dummy_index in range(length)]
        for index in range(length):
            left_max[index] = max(left_max_val, height[index])
            left_max_val = left_max[index]
            right_max[length - 1 - index] = max(right_max_val, height[length - 1 - index])
            right_max_val = right_max[length - 1 - index]
        result = 0
        for index in range(length):
            result += min(left_max[index], right_max[index]) - height[index] 
        return result

if __name__ == '__main__':
    pass