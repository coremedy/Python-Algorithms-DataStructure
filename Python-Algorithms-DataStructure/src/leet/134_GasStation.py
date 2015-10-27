'''
Created on 2015-10-26
'''


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        : if index is the right answer, any subarray ranging from index to len(gas) - 1 should have a sum >= 0
        """
        total_sum, local_sum, candidate = 0, 0, 0
        for index in range(len(gas)):
            total_sum, local_sum = total_sum + gas[index] - cost[index], local_sum + gas[index] - cost[index]
            if local_sum < 0:
                local_sum, candidate = 0, index + 1
        if total_sum < 0 or candidate == len(gas):
            return -1
        return candidate

if __name__ == '__main__':
    pass