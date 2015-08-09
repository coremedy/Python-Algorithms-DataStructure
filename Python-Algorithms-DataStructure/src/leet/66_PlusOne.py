'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if digits is None:
            return digits
        if len(digits) == 0:
            return digits
        digits[-1], carry = (digits[-1] + 1) % 10, (digits[-1] + 1) // 10
        for index in range(len(digits) - 2, -1, -1):
            if carry == 0:
                return digits
            digits[index], carry = (digits[index] + carry) % 10, (digits[index] + carry) // 10
        if carry == 0:
            return digits
        return [carry] + digits

if __name__ == '__main__':
    pass