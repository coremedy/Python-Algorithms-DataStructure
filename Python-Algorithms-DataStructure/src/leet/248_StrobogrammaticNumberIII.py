'''
Created on 2015-10-12
'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Base case
        if n == 0:
            return []
        elif n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ['11', '69', '88', '96']
        result = []
        for s in (['0', '1', '8'] if n % 2 == 1 else ['00', '11', '69', '88', '96']):
            self.dfs(s, len(s), n, result)
        return result
    
    def dfs(self, s, i, n, result):
        if i == n:
            result.append(s)
        else:
            if n - i > 2:
                self.dfs('0' + s + '0', i + 2, n, result)
            self.dfs('1' + s + '1', i + 2, n, result)
            self.dfs('6' + s + '9', i + 2, n, result)
            self.dfs('8' + s + '8', i + 2, n, result)
            self.dfs('9' + s + '6', i + 2, n, result)    
    
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count = 0
        for l in range(len(low), len(high) + 1):
            for s in self.findStrobogrammatic(l):
                if len(low) == len(high):
                    if s >= low and s <= high:
                        count += 1
                elif len(s) == len(low) and s >= low:
                    count += 1
                elif len(s) == len(high) and s <= high:
                    count += 1
                elif len(s) > len(low) and len(s) < len(high):
                    count += 1
        return count

if __name__ == '__main__':
    pass