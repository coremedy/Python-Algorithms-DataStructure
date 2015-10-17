'''
Created on 2015-10-17
'''

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) < 2:
            return result
        for index in range(len(s) - 1):
            if s[index : index + 2] == '++':
                result.append(s[:index] + '--' + s[index + 2:])
        return result

if __name__ == '__main__':
    pass