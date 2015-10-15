'''
Created on 2015-10-15
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_len = len(s)
        if str_len == 0 or numRows <= 0:
            return ''
        if numRows == 1 or str_len <= numRows :
            return s
        result = ['' for dummy_i in range(numRows)]
        pos, inc = -1, 1
        for index in range(str_len):
            result[pos + inc], pos, inc = result[pos + inc] + s[index], pos + inc, inc * -1 if index > 0 and index % (numRows - 1) == 0 else inc
        return ''.join(result)

if __name__ == '__main__':
    pass