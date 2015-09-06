'''
Created on 2015-09-06
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        base_lft, count = 1, 0
        while base_lft <= x:
            base_lft, count = base_lft * 10, count + 1
        base_lft, count = base_lft // 10, count // 2
        while count > 0:
            if (x // base_lft) % 10 != x % 10:
                return False
            base_lft, x, count = base_lft // 100, x // 10, count - 1
        return True

if __name__ == '__main__':
    pass