'''
Created on 2015-09-05
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :Finite State Machine
        """
        if len(str) == 0:
            return 0
        state, postive, values = 0, True, []
        for ch in str:
            if state == 0:
                if ch == '+' or ch == '-':
                    state, postive = 1, False if ch == '-' else True
                elif ch.isdigit():
                    state = 2
                    values.append(ord(ch) - 48)                   
                elif ch.isspace():
                    continue
                else:
                    return 0
            elif state == 1:
                if ch.isdigit():
                    state = 2
                    values.append(ord(ch) - 48)
                else:
                    return 0
            elif state == 2:
                if ch.isdigit():
                    values.append(ord(ch) - 48)
                else:
                    break
        if len(values) > 10:
            return 2147483647 if postive else -2147483648
        table, result = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1], 0
        for index in range(10 - len(values), 10):
            result += table[index] * values[index - 10 + len(values)]
        result = result if postive else -result
        return -2147483648 if result < -2147483648 else (2147483647 if result > 2147483647 else result)

if __name__ == '__main__':
    pass