'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1, 1]
        for dummy_index in range(2, rowIndex + 1):
            temp = result[0]
            for index in range(1, len(result)):
                temp, result[index] = result[index], result[index] + temp
            result.append(1)
        return result

if __name__ == '__main__':
    pass