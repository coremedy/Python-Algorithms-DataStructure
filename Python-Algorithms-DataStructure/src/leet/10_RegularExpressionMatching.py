'''
Created on 2015-07-21
'''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        p_length = len(p)
        s_length = len(s)
        if p_length == 0:
            if s_length == 0:
                return True
            else:
                return False
        new_p = self.parse_pattern(p)
        p_length = len(new_p)
        table = [[False for dummy_col in range(s_length + 1)] for dummy_row in range(p_length + 1)]
        # Empty pattern and empty string
        table[0][0] = True
        # Non-empty pattern and empty string
        for row in range(1, p_length + 1):
            if len(new_p[row - 1]) == 2 and table[row - 1][0]:
                table[row][0] = True
        # DP start
        for row in range(1, p_length + 1):
            for col in range(1, s_length + 1):
                if table[row - 1][col - 1]:
                    if new_p[row - 1][0] == s[col - 1] or new_p[row - 1][0] == '.':
                        table[row][col] = True
                        continue
                if table[row][col - 1]:
                    if len(new_p[row - 1]) == 2:
                        if new_p[row - 1][0] == s[col - 1] or new_p[row - 1][0] == '.':
                            table[row][col] = True
                            continue
                if table[row - 1][col]:
                    if len(new_p[row - 1]) == 2:
                        table[row][col] = True
        return table[p_length][s_length]

    def parse_pattern(self, p):
        stack = list(p)
        result = []
        while len(stack):
            token = stack.pop()
            if token == '*':
                token = stack.pop() + token
            result.append(token)
        result.reverse()
        return result

if __name__ == '__main__':
    pass