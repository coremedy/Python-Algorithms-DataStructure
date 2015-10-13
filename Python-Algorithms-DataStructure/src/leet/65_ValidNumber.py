'''
Created on 2015-10-13
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # This is a problem that can be solved by DFA
        # http://images.cnitblog.com/i/627993/201405/012016243309923.png
        INVALID, SPACE, DIGIT, SIGN, DOT, EXP = 0, 1, 2, 3, 4, 5
        STATE_TRANSITION_TABLE = [[-1,  0,  1,  2,  3, -1],
                                  [-1,  8,  1, -1,  4,  5],
                                  [-1, -1,  1, -1,  3, -1],
                                  [-1, -1,  4, -1, -1, -1],
                                  [-1,  8,  4, -1, -1,  5],
                                  [-1, -1,  7,  6, -1, -1],
                                  [-1, -1,  7, -1, -1, -1],
                                  [-1,  8,  7, -1, -1, -1],
                                  [-1,  8, -1, -1, -1, -1]]
        # STATEs 1, 4, 7, 8 are valid ending states
        state = 0 
        for ch in s:
            input_type = INVALID
            if ch == ' ':
                input_type = SPACE
            elif ch in '0123456789':
                input_type = DIGIT
            elif ch in '+-':
                input_type = SIGN
            elif ch == '.':
                input_type = DOT
            elif ch in 'eE':
                input_type = EXP
            state = STATE_TRANSITION_TABLE[state][input_type]
            if state == -1:
                return False
        return state == 1 or state == 4 or state == 7 or state == 8

if __name__ == '__main__':
    pass