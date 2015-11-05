'''
Created on 2015-11-05
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        table = []
        for ch in s:
            if ch == '(':
                table.append(ch)
            elif ch == ')':
                if table and table[-1] == '(':
                    table.pop()
                else:
                    table.append(ch)
        if not table:
            return [s]
        self.result, self.s, self.s_len = set(), s, len(s)
        self.dfs(table.count('('), table.count(')'), 0, '')
        return list(self.result)

    def dfs(self, left, right, index, tmp):
        def checkValidness(s):
            count = 0
            for ch in s:
                count = (count + 1) if ch == '(' else ((count - 1) if ch == ')' else count)
                if count < 0:
                    return False
            return True if not count else False
        
        if index == self.s_len:
            if (left + right) == 0 and checkValidness(tmp):
                self.result.add(tmp)
        else:
            if left + right == 0:
                curr = tmp + self.s[index:]
                if checkValidness(curr):
                    self.result.add(curr)
            elif (left + right) <= (self.s_len - index):
                if self.s[index] == '(' and left > 0:
                    self.dfs(left - 1, right, index + 1, tmp)
                elif self.s[index] == ')' and right > 0:
                    self.dfs(left, right - 1, index + 1, tmp)
                self.dfs(left, right, index + 1, tmp + self.s[index])

if __name__ == '__main__':
    pass