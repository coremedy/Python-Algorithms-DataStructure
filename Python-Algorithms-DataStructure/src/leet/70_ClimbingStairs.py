'''
Created on 2015-07-16
'''
# FIB?
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            ways = [1, 1]
            for step in range(2, n + 1):
                ways.append(ways[step - 1] + ways[step - 2])
            return ways[n]

if __name__ == '__main__':
    pass