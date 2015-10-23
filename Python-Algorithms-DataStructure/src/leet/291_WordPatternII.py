'''
Created on 2015-10-23
'''

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.pattern, self.pattern_len, self.str, self.str_len, self.done, self.d, self.r = pattern, len(pattern), str, len(str), False, dict(), dict()
        if self.pattern_len == 0 and self.str_len == 0:
            return True
        elif self.pattern_len == 0 or self.str_len == 0:
            return False
        self.dfs(0, self.pattern_len - 1, 0, self.str_len - 1)
        return self.done
        
    def dfs(self, pattern_beg, pattern_end, str_beg, str_end):
        if pattern_beg > pattern_end and str_beg > str_end:
            self.done = True
        elif pattern_beg <= pattern_end and str_beg <= str_end:
            p = self.pattern[pattern_beg : pattern_beg + 1]
            if p in self.d:
                if len(self.d[p]) <= str_end - str_beg + 1 and self.d[p] == self.str[str_beg : str_beg + len(self.d[p])]:
                    self.dfs(pattern_beg + 1, pattern_end, str_beg + len(self.d[p]), str_end)
            else:
                for l in range(1, str_end - str_beg + 2):
                    if self.done:
                        return                    
                    s = self.str[str_beg : str_beg + l]
                    if s not in self.r:
                        self.r[s] = p
                        self.d[p] = s
                        self.dfs(pattern_beg + 1, pattern_end, str_beg + l, str_end)
                        self.d.pop(p, None)
                        self.r.pop(s, None)

if __name__ == '__main__':
    pass