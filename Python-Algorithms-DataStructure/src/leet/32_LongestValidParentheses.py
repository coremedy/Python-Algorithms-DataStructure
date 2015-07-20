'''
Created on 2015-07-19

DP: table[i] represents the max valid substring starting at i
    if s[i] == ')' table[i] will be zero because no valid string starts with ')'
    if s[i] == '(' then string can be like this '( table[i+1] )', just find the first right match
                   and chain the valid string after the right match
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses_dp(self, s):
        if len(s) == 0:
            return 0
        table = [0 for dummy_i in range(len(s))]
        for index in range(len(s) - 2, -1, -1):
            if s[index] == ')':
                table[index] = 0
            else:
                next_match = index + table[index + 1] + 1
                if next_match < len(s) and s[next_match] == ')':
                    table[index] = table[index + 1] + 2
                    if next_match + 1 < len(s):
                        table[index] += table[next_match + 1]
        return max(table)
    
    # @param {string} s
    # @return {integer}
    def longestValidParentheses_raw(self, s):
        if len(s) == 0:
            return 0
        stack = []
        for index in range(len(s)):
            if s[index] == '(':
                stack.append(-1)
            else:
                if len(stack) == 0:
                    stack.append(-2)
                else:
                    if stack[-1] == -2:
                        stack.append(-2)
                    elif stack[-1] == -1:
                        stack.pop()
                        stack.append(2)
                        self.merge_substr(stack)
                    else:
                        self.merge_substr(stack)
                        if len(stack) == 1:
                            stack.append(-2)
                        else:
                            if stack[len(stack) - 2] == -1:
                                value = stack.pop()
                                stack.pop()
                                stack.append(value + 2)
                                self.merge_substr(stack)
                            else:
                                stack.append(-2)
        result = 0
        for index in range(len(stack)):
            if stack[index] > result:
                result = stack[index]
        return result
        
    def merge_substr(self, stack):
        value = stack.pop()
        while len(stack) > 0:
            if stack[-1] > 0:
                value += stack.pop()
            else:
                break
        stack.append(value)

if __name__ == '__main__':
    pass