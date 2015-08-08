'''
Created on 2015-08-07
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if s is None:
            return True
        if len(s) == 0:
            return True
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                continue
            if not stack:
                return False
            if stack:
                if (ch == ')' and stack[-1] == '(') or (ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0)

if __name__ == '__main__':
    pass