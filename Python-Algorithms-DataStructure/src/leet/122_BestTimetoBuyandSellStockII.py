'''
Created on 2015-08-16
'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        result = 0
        prev = prices[0]
        for index in range(1, len(prices)):
            if prices[index] - prev > 0:
                result += prices[index] - prev
            prev = prices[index]
        return result

if __name__ == '__main__':
    pass