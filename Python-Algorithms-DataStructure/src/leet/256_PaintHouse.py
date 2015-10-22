'''
Created on 2015-10-22
'''

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs_len = len(costs)
        if costs_len == 0:
            return 0
        elif costs_len == 1:
            return min(costs[0])
        for index in range(1, costs_len):
            costs[index][0] += min(costs[index - 1][1], costs[index - 1][2])
            costs[index][1] += min(costs[index - 1][0], costs[index - 1][2])
            costs[index][2] += min(costs[index - 1][0], costs[index - 1][1])
        return min(costs[-1])

if __name__ == '__main__':
    pass