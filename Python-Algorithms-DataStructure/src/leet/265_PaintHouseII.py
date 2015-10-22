'''
Created on 2015-10-22
'''

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        if k == 0:
            return 0
        elif k == 1:
            if n == 1:
                return costs[0][0]
            return 0
        prev = self.getMins(costs[0])
        for index in range(1, n):
            for color_index in range(k):
                if costs[index - 1][color_index] > prev[0]:
                    costs[index][color_index] += prev[0]
                elif costs[index - 1][color_index] == prev[0]:
                    costs[index][color_index] += prev[0] if prev[1] > 1 else prev[2]
            prev = self.getMins(costs[index])
        return prev[0]

    def getMins(self, cost):
        result = [cost[0], 1, 2147483647]
        for index in range(1, len(cost)):
            if cost[index] == result[0]:
                result[1] += 1
            elif cost[index] < result[0]:
                result[2], result[1], result[0] = result[0], 1, cost[index]
            else:
                result[2] = cost[index] if cost[index] < result[2] else result[2]
        return result 

if __name__ == '__main__':
    pass