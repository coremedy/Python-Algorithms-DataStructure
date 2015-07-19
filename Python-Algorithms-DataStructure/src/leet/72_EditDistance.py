'''
Created on 2015-07-19

Old problem: Edit Distance/Levenstein Distance/DNA Distance ...
             Break it down
                            ""  A   B    C  (TOP ROW)
             ""             0   1   2    3
             A              1
             B              2
             (BUTTOM ROW)
             
             When "" meets "", of course the distance is 0
             When "" meets any non-empty string, the distance is the length of the string
             Let's look at cell (1, 1)
             Three conditions here:
             1.   ""  (DISTANCE 1)    ->     "" A    DISTANCE 1 + 1
                  A   (REPLACE)              A  -    (INSERTION)
             
             2.   A   (DISTANCE 1)    ->     A  -    DISTANCE 1 + 1
                  ""  (REPLACE)              "" A    (DELETION)
                  
             3.   ""  (DISTANCE 0)    ->     "" A    DISTANCE 0 + 0
                  ""  (EQUAL)                "" A    (EQUAL)
             But on algorithm books, we describe the recursion formula from right to left,
             that's why you see they mention gap (-) in their books
'''

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        word1_length = len(word1)
        word2_length = len(word2)
        table = [[0 for dummy_col in range(word1_length + 1)] for dummy_row in range(word2_length + 1)]
        for col in range(1, word1_length + 1):
            table[0][col] = col
        for row in range(1, word2_length + 1):
            table[row][0] = row
        for row in range(1, word2_length + 1):
            for col in range(1, word1_length + 1):
                val = 0
                if word1[col - 1] != word2[row - 1]:
                    val = 1
                table[row][col] = min(table[row][col - 1] + 1, table[row - 1][col] + 1, table[row - 1][col - 1] + val)
        return table[word2_length][word1_length]

if __name__ == '__main__':
    pass