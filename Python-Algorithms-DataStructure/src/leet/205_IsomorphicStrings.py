'''
Created on 2015-08-30
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        d = dict()
        for index in range(len(s)):
            if d.get(s[index], None) is None:
                if t[index] in d.values():
                    return False
                else:
                    d[s[index]] = t[index]
            elif d[s[index]] != t[index]:
                return False
        return True

if __name__ == '__main__':
    pass