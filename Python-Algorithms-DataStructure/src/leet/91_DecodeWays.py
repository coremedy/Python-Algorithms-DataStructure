'''
Created on 2015-07-17
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s == '0':
                return 0
            return 1
        else:
            if s[0 : 1] == '0':
                return 0
            record = set(['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
            table = [0 for dummy_i in range(0, len(s) + 1)]
            table[0] = 1
            table[1] = 1
            for index in range(2, len(s) + 1):
                if s[index - 1 : index] == '0':
                    if s[index - 2 : index] in record:
                        table[index] += table[index - 2]
                    else:
                        return 0
                else:
                    table[index] = table[index - 1]
                    if s[index - 2 : index] in record:
                        table[index] += table[index - 2]
            return table[len(s)]

if __name__ == '__main__':
    pass