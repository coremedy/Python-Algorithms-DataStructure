'''
Created on 2015-09-05
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a, length_b, length_max, carry, result = len(a), len(b), max(len(a), len(b)), 0, ['' for dummy_index in range(max(len(a), len(b)) + 1)]
        for index in range(length_max):
            value = (ord(a[length_a - 1 - index]) - 48 if length_a - 1 - index >= 0 else 0) + (ord(b[length_b - 1 - index]) - 48 if length_b - 1 - index >= 0 else 0) + carry
            carry, value = value // 2, value % 2
            result[length_max - index] = chr(value + 48)
        result[0] = '1' if carry == 1 else ''
        return ''.join(result)

if __name__ == '__main__':
    pass