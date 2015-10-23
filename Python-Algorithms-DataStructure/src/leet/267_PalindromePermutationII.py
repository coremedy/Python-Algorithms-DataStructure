'''
Created on 2015-10-24
'''

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_len = len(s)
        if s_len == 0:
            return []
        elif s_len == 1:
            return [s]
        if not self.decide(s, s_len):
            return []
        self.result = []
        self.dfs(self.cand, '')
        return self.result    
    
    def dfs(self, cur, tgt):
        if len(cur) == 0:
            self.result.append(tgt[::-1] + self.mid + tgt)
        else:
            index, cur_len = 0, len(cur)
            while index < cur_len:
                self.dfs(cur[:index] + cur[index + 1:], tgt + cur[index])
                index += 1
                while index < cur_len and cur[index - 1] == cur[index]:
                    index += 1
    
    def decide(self, s, s_len):
        d, odd_count = dict(), 0
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
            odd_count = (odd_count + 1) if d[ch] % 2 == 1 else (odd_count - 1)
        if (s_len % 2 == 0 and odd_count != 0) or (s_len % 2 == 1 and odd_count != 1):
            return False
        tmp, self.mid = [], ''
        for k, v in d.items():
            tmp, self.mid = tmp + [k] * (v // 2), k if v % 2 == 1 else self.mid
        self.cand = ''.join(sorted(tmp))
        return True

if __name__ == '__main__':
    pass