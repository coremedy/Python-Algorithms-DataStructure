'''
Created on 2015-10-09
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        index, result = 0, ''
        while num != 0:
            while num >= a[index]:
                num -= a[index]
                result += d[index]
            index += 1
        return result

if __name__ == '__main__':
    pass