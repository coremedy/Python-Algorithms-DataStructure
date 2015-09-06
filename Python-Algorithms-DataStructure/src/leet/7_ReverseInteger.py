'''
Created on 2015-09-06
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        positive, x, base, result, count = 1 if x > 0 else -1, x if x > 0 else -x, 1, 0, 0
        while base <= x:
            base, count = base * 10, count + 1
        base /= 10
        while count > 0:
            result, x, base, count = result + (x % 10) * base, x // 10, base / 10, count - 1
            if (positive * result > 2147483647) or (positive * result < -2147483648):
                return 0
        return positive * result

if __name__ == '__main__':
    pass