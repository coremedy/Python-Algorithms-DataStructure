'''
Created on 2015-10-23
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_len, str_array = len(pattern), str.split(' ')
        if pattern_len != len(str_array):
            return False
        d, r = dict(), dict()
        for index in range(pattern_len):
            if str_array[index] not in r:
                if pattern[index] in d:
                    return False
                else:
                    d[pattern[index]] = str_array[index]
                r[str_array[index]] = pattern[index]
            else:
                if r[str_array[index]] != pattern[index]:
                    return False
        return True

if __name__ == '__main__':
    pass