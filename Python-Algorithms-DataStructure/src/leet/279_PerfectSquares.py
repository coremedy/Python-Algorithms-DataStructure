'''
Created on 2015-10-10
'''

class Solution(object):
    # Static DP - avoiding dup calculation
    _table = [0, 1, 2, 3]
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= len(self._table) - 1:
            return self._table[n]
        base, start = 2, len(self._table)
        self._table += [dummy_index for dummy_index in range(start, n + 1)]
        while base * base <= n:
            s = base * base
            for index in range(start, n + 1):
                self._table[index] = min(self._table[index], index // s + self._table[index % s])
            base += 1
        return self._table[n]

if __name__ == '__main__':
    pass