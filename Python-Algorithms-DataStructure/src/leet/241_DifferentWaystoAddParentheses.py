'''
Created on 2015-10-20
"2*3-4*5"
The first 'divide' step is to change the input to (2) * (2*3-4*5), not to (2*3)-4*5
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.dfs(input, 0, len(input) - 1)

    def dfs(self, input, beg, end):
        result = []
        for index in range(beg, end):
            if input[index] in '+-*':
                self.calc(self.dfs(input, beg, index - 1), self.dfs(input, index + 1, end), input[index], result)
        return result if len(result) > 0 else [int(input[beg : end + 1])]

    def calc(self, left, right, ops, result):
        for l in left:
            for r in right:
                result.append((l + r) if ops == '+' else ((l - r) if ops == '-' else (l * r)))
    

if __name__ == '__main__':
    pass