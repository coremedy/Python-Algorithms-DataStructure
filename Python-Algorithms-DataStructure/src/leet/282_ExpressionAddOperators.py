'''
Created on 2015-10-21
'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.nums, self.nums_len, self.tgt, self.res = num, len(num), target, []
        if self.nums_len > 0:
            self.dfs(0, self.nums_len - 1, 0, False, False, 1, '')
        return self.res

    def dfs(self, beg, end, tmp, neg, mul, opr, exp):
        for index in range(beg, end):
            s = self.nums[beg : index + 1]
            s_val = int(s)
            self.dfs(index + 1, end, tmp + (-1 if neg else 1) * (opr if mul else 1) * s_val, False, False, 1, exp + s + '+')
            self.dfs(index + 1, end, tmp + (-1 if neg else 1) * (opr if mul else 1) * s_val, True, False, 1, exp + s + '-')
            self.dfs(index + 1, end, tmp, neg, True, (opr if mul else 1) * s_val, exp + s + '*')
            if self.nums[beg] == '0':
                break
        if beg == end or self.nums[beg] != '0':
            if tmp + (-1 if neg else 1) * (opr if mul else 1) * int(self.nums[beg : end + 1]) == self.tgt:
                self.res.append(exp + self.nums[beg : end + 1])

if __name__ == '__main__':
    pass