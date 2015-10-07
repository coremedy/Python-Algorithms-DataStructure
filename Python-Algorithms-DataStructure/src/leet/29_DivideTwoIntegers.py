'''
Created on 2015-10-07
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign, dividend, divisor, result = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else False, abs(dividend), abs(divisor), 0
        if divisor > dividend:
            return result
        while dividend >= divisor:
            cnt, tmp = 1, divisor
            while (tmp << 1) <= dividend:
                tmp, cnt = tmp << 1, cnt + 1
            dividend, result = dividend - tmp, result + (1 << cnt - 1)
        # The range of INT is -0x80000000 to 0x7FFFFFFF and there is no positive 0x80000000 for INT
        # -(-0x80000000) = NOT(-0x80000000) + 1 = 0x7FFFFFFF + 1
        # But there is no 0x80000000 for INT so the result is undefined
        if result == 0x80000000 and sign:
            return 0x7FFFFFFF
        return result if sign else -result

if __name__ == '__main__':
    pass