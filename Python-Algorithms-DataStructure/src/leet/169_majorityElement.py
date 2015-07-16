'''
Created on 2015-01-31
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        d = {}        
        for i in num:
            if not d.get(i):
                d[i] = 1
            else:
                d[i] += 1
        for j in d.keys():
            if d[j] > (len(num) // 2):
                return j

if __name__ == '__main__':
    pass