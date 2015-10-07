'''
Created on 2015-10-07
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        result, index = [0] * (len(num1) + len(num2) + 1), 0
        for ch1 in reversed(num1):
            inner_index, carry1, carry2 = 0, 0, 0
            for ch2 in reversed(num2):
                tmp = (ord(ch1) - 0x30) * (ord(ch2) - 0x30) + carry1
                tmp, carry1 = tmp % 10, tmp // 10
                r = result[index + inner_index] + tmp + carry2
                result[index + inner_index], carry2, inner_index = r % 10, r // 10, inner_index + 1
            result[index + inner_index], index = result[index + inner_index] + carry1 + carry2, index + 1
        while result[-1] == 0:
            result.pop()
        return ''.join(str(x) for x in reversed(result))

if __name__ == '__main__':
    pass