'''
Created on 2015-07-26
'''

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        else:
            data_table = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
            input_table = []
            for index in range(len(digits)):
                if int(digits[index]) != 0 and int(digits[index]) != 1:
                    input_table.append(data_table[int(digits[index])])
            if len(input_table) == 0:
                return []
            else:
                result = []
                self.backTrack(input_table, 0, result, [])
                return result
    
    def backTrack(self, input_table, depth, result, cache):
        # Baseline
        if depth == len(input_table):
            result.append(''.join(cache))
        else:
            for s in input_table[depth]:
                cache.append(s)
                self.backTrack(input_table, depth + 1, result, cache)
                cache.pop()
        
if __name__ == '__main__':
    pass