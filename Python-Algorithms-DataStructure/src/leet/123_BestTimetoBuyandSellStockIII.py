'''
Created on 2015-07-20
'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        prices_length = len(prices)
        if prices_length == 0 or prices_length == 1:
            return 0
        # If the stock is sold today, what's the max profit
        max_sell_at = [0 for dummy_i in range(prices_length)]
        max_sell_at[0] = prices[0]
        # If the stock is bought today, what's the max profit
        max_buy_at = [0 for dummy_i in range(prices_length)]
        max_buy_at[-1] = prices[-1]
        for index in range(1, prices_length):
            max_sell_at[index] = min(max_sell_at[index - 1], prices[index])
            max_buy_at[prices_length - 1 - index] = max(max_buy_at[prices_length - index], prices[prices_length - 1 - index])
        result = 0
        for index in range(0, prices_length):
            max_sell_at[index] = prices[index] - max_sell_at[index]
            result = max(result, max_sell_at[index])
            max_buy_at[index] = max_buy_at[index] - prices[index]
            result = max(result, max_buy_at[index])
        for index in range(1, len(prices)):
            # If the stock is sold from beginning to today, what's the max profit
            max_sell_at[index] = max(max_sell_at[index - 1], max_sell_at[index])
            # If the stock is bought from today to end, what's the max profit
            max_buy_at[prices_length - 1 - index] = max(max_buy_at[prices_length - index], max_buy_at[prices_length - 1 - index])
        # Final DP
        for index in range(0, prices_length - 1):
            result = max(max_sell_at[index] + max_buy_at[index + 1], result)
        return result

if __name__ == '__main__':
    pass