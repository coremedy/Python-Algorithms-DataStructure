'''
Created on 2015-10-17
CanWin means the current move can lead to winning status
'Guarantee a win' means you win no matter how the other play make the move
'''

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        for index in range(len(s) - 1):
            if s[index : index + 2] == '++' and not self.canWin(s[:index] + '--' + s[index + 2:]):
                return True
        return False

if __name__ == '__main__':
    pass