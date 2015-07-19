'''
Created on 2015-07-19

Dynamic programming O(n^4):

IS_SCRAMBLE_STR[k][i][j] = 
            IS_SCRAMBLE_STR[sub_str_len_less_than_k][i][j] && IS_SCRAMBLE_STR[k - sub_str_len_less_than_k][i + sub_str_len_less_than_k][j + sub_str_len_less_than_k]
            OR
            IS_SCRAMBLE_STR[sub_str_len_less_than_k][i][j + k - sub_str_len_less_than_k] && IS_SCRAMBLE_STR[k - sub_str_len_less_than_k][i + sub_str_len_less_than_k][j]
            for all sub_str_len_less_than_k 
'''

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1_list = list(s1)
        s2_list = list(s2)
        s1_list.sort()
        s2_list.sort()
        if s1_list != s2_list:
            return False
        s1_length = len(s1)
        for index in range(1, s1_length):
            if self.isScramble(s1[:index], s2[:index]) and self.isScramble(s1[index:], s2[index:]):
                return True
            if self.isScramble(s1[:index], s2[s1_length - index:]) and self.isScramble(s1[index:], s2[:s1_length - index]):
                return True
        return False

if __name__ == '__main__':
    pass