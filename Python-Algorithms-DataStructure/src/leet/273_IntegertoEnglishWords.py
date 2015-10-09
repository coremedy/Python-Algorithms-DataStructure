'''
Created on 2015-10-09
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        single = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine']
        double_less_than_twenty = [' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        double = ['', '', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        quad = ['', ' Thousand', ' Million', ' Billion']
        quad_index, result, tmp, num = 0, '', num % 1000, num // 1000
        while tmp != 0 or num != 0:
            result = ('' if tmp // 100 == 0 else (single[tmp // 100] + ' Hundred')) + ((double_less_than_twenty[tmp % 10]) if tmp % 100 > 9 and tmp % 100 < 20 else (double[(tmp % 100) // 10] + single[(tmp % 10)])) + (quad[quad_index] if tmp != 0 else '') + result
            num, quad_index, tmp  = num // 1000, quad_index + 1, num % 1000
        return result if result[0] != ' ' else result[1:]

if __name__ == '__main__':
    pass