'''
Created on 2015-10-23
'''

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []
        self.result = []
        self.dfs(2, n, [])
        return self.result
        
    def dfs(self, beg, target, tmp):
        if beg * beg <= target:
            while beg * beg <= target:
                if target % beg == 0:
                    self.result.append(tmp[:] + [beg, target // beg])
                    self.dfs(beg, target // beg, tmp + [beg])
                beg += 1

if __name__ == '__main__':
    pass