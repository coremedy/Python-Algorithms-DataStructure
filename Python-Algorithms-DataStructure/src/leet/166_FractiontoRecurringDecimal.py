'''
Created on 2015-08-30
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return None
        sign, numerator, denominator = "" if numerator * denominator >= 0 else "-", numerator if numerator >= 0 else -numerator, denominator if denominator >= 0 else -denominator
        result, nums, d, index, location = str(numerator // denominator), [], dict(), 0, None
        if numerator % denominator == 0:
            return sign + result
        while True:
            numerator, index = 10 * (numerator % denominator), index + 1
            nums.append(str(numerator // denominator))
            if numerator == 0:
                break
            location = d.get(numerator)
            if location is not None:
                break
            d[numerator] = index - 1
        remainder = ''.join(nums[:index - 1]) if numerator == 0 else ''.join(nums[:location]) + '(' + ''.join(nums[location: index - 1]) + ')'
        return sign + result + '.' + remainder

if __name__ == '__main__':
    pass