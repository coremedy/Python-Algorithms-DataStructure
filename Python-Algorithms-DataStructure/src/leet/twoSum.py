'''
Created on 2014-12-26
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if (target - num[i]) in d:
                return (d[target - num[i]] + 1, i + 1)
            else:
                d[num[i]] = i

if __name__ == '__main__':
    pass