'''
Created on 2015-08-13
Make the tow boards larger and larger ...
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result

if __name__ == '__main__':
    pass