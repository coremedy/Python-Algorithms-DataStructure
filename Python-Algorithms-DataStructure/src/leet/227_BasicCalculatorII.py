'''
Created on 2015-10-16
Change to RPN
But you need to calculate from left to right, so ... reverse
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_buffer, token_buffer, result = '', [], []
        for ch in reversed(s):
            num_buffer = ch + num_buffer if ch.isdigit() else num_buffer
            if ch in '*/+-':
                result.append(int(num_buffer))
                num_buffer = ''
                if ch in '+-' and len(token_buffer) > 0 and token_buffer[-1] in '*/':
                    self.calc(token_buffer, result, False)
                token_buffer.append(ch)
        result.append(int(num_buffer))
        if len(token_buffer) > 0:
            self.calc(token_buffer, result, True)
        return result[0]
        
    def calc(self, token_buffer, result, clear):
        while len(token_buffer) > 0:
            if token_buffer[-1] in '+-' and not clear:
                return
            ch, a, b = token_buffer.pop(), result.pop(), result.pop()
            result.append((a // b) if ch == '/' else ((a * b) if ch == '*' else ((a + b) if ch == '+' else (a - b))))
        return

if __name__ == '__main__':
    pass