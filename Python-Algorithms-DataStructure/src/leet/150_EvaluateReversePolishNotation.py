'''
Created on 2015-08-07
'''

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
            if not tokens:
                return None
            stack = []
            for t in tokens:
                if t == '+':
                    if len(stack) < 2:
                        return None
                    rhs = stack.pop()
                    lhs = stack.pop()
                    stack.append(lhs + rhs)
                    continue
                if t == '-':
                    if len(stack) < 2:
                        return None
                    rhs = stack.pop()
                    lhs = stack.pop()
                    stack.append(lhs - rhs)
                    continue
                if t == '*':
                    if len(stack) < 2:
                        return None                
                    rhs = stack.pop()
                    lhs = stack.pop()
                    stack.append(lhs * rhs)
                    continue
                if t == '/':
                    if len(stack) < 2:
                        return None                
                    rhs = stack.pop()
                    if rhs == 0:
                        return None                
                    lhs = stack.pop()
                    if rhs * lhs < 0:
                        stack.append(-((-lhs) / rhs))
                    else:
                        stack.append(lhs / rhs)                
                    continue
                stack.append(int(t))
            return stack[0]

if __name__ == '__main__':
    pass