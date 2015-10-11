'''
Created on 2015-10-11
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        n, table, index1, index2, index3 = n - 1, [1], 0, 0, 0
        while n > 0:
            a, b, c = table[index1] * 2, table[index2] * 3, table[index3] * 5
            minimal = min(a, b, c)
            index1, index2, index3 = index1 + 1 if minimal == a else index1, index2 + 1 if minimal == b else index2, index3 + 1 if minimal == c else index3
            if minimal > table[-1]:
                table.append(minimal)
                n -= 1
        return table[-1]

if __name__ == '__main__':
    pass