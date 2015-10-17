'''
Created on 2015-10-17
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        diff = abs(len(s) - len(t))
        if diff >= 2:
            return False
        if len(s) == 0 and len(t) == 0:
            return False
        if len(s) == 0 or len(t) == 0:
            return True        
        if diff == 1:
            count, index_s, index_t = 0, 0, 0
            while index_s < len(s) and index_t < len(t):
                if s[index_s] != t[index_t]:
                    if count > 0:
                        return False
                    else:
                        index_s, index_t, count = index_s + 1 if len(s) > len(t) else index_s, index_t + 1 if len(t) > len(s) else index_t, count + 1
                else:
                    index_s, index_t = index_s + 1, index_t + 1
            return True
        else:
            count = 0
            for index in range(len(s)):
                if s[index] != t[index]:
                    count += 1
            return True if count == 1 else False

if __name__ == '__main__':
    pass