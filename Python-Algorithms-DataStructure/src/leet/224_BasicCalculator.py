'''
Created on 2015-08-07
Dirty
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        token_stack = []
        parentheses_stack = []
        index = 0
        s = '(' + s.strip() + ')'
        while index < len(s):
            token = s[index]
            if token == '(' or token == '+' or token == '-':
                token_stack.append(token)
                if token == '(':
                    parentheses_stack.append(len(token_stack) - 1)
                index += 1
            elif token == ')':
                pos = parentheses_stack.pop()
                if pos == len(token_stack) - 1:
                    token_stack.pop()
                else:
                    val = token_stack.pop()
                    token_stack.pop()
                    token_stack.append(self.calc_helper(token_stack, val))
                index += 1
            else:
                next_pos = index + 1
                while next_pos < len(s):
                    if s[next_pos] == '(' or s[next_pos] == ')' or s[next_pos] == '+' or s[next_pos] == '-':
                        break
                    else:
                        next_pos += 1
                token_stack.append(self.calc_helper(token_stack, int(s[index:next_pos])))
                index = next_pos
                
        return token_stack[0]
        
    def calc_helper(self, token_stack, val):
        if len(token_stack) >= 2:
            if token_stack[-1] == '+':
                token_stack.pop()
                val += token_stack.pop()
            elif token_stack[-1] == '-':
                token_stack.pop()
                lhs = token_stack.pop()
                val = lhs - val
        return val


if __name__ == '__main__':
    pass