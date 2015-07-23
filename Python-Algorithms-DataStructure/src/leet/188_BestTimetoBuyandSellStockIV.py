'''
Created on 2015-07-23
'''

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        # Two input: k and prices list
        # Try to find sub-problem related to k - 1 and len(prices) - 1
        # The tricky part is: we don't directly use k, we use 2k, since k transactions need 2k operations (buy and sell)
        prices_len = len(prices)
        if k > (prices_len // 2):
            sum = 0
            # Buy stock today, sell stock tomorrow, and then buy stock tomorrow ...
            for index in range(1, prices_len):
                if prices[index] > prices[index - 1]:
                    sum += prices[index] - prices[index - 1]
            return sum
        else:
            number_of_purchase_and_sell = 2 * k
            table = [[-4294967296 for dummy_col in range(number_of_purchase_and_sell + 1)] for dummy_row in range(prices_len)]
            for row in range(prices_len):
                # 0 purchase and 0 sell
                table[row][0] = 0
                # Go through elements of prices
                for col in range(min(number_of_purchase_and_sell, row + 1), 0, -1):
                    if not row:
                        table[row][col] = max(table[row][col], table[row][col - 1] + prices[row] * [1, -1][col % 2])
                    # Either we re-use the result of smaller problem (ignore the current element of prices)
                    # Or we use the the current element of prices to form valid transactions
                    else:
                        table[row][col] = max(table[row - 1][col], table[row - 1][col - 1] + prices[row] * [1, -1][col % 2])
            return max(table[prices_len - 1])

if __name__ == '__main__':
    pass