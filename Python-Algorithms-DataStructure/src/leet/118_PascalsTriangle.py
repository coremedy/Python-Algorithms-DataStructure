'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for dummy_index in range(3, numRows + 1):
            temp_result = [1]
            for index in range(0, len(result[-1]) - 1):
                temp_result.append(result[-1][index] + result[-1][index + 1])
            temp_result.append(1)
            result.append(temp_result)
        return result

if __name__ == '__main__':
    pass