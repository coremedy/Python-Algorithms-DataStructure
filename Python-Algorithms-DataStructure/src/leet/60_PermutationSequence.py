'''
Created on 2015-07-27
'''

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        table = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        array = [index for index in range(1, n + 1)]
        k -= 1
        result = []
        while len(array) > 0:
            index = k // table[n - 1]
            result.append(str(array[index]))
            k = k % table[n - 1]
            n -= 1
            array = array[:index] + array[index + 1:]
        return ''.join(result)

if __name__ == '__main__':
    pass