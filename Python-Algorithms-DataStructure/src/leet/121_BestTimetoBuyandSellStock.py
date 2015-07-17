'''
Created on 2015-07-17
'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        else:
            min_prices = [0 for dummy_i in range(0, len(prices))]
            min_prices[0] = prices[0]
            result = 0
            for index in range(1, len(prices)):
                min_prices[index] = min(min_prices[index - 1], prices[index])
                result = max(result, prices[index] - min_prices[index])
            return result

if __name__ == '__main__':
    pass