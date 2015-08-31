'''
Created on 2015-08-31
This is another instance of key generation
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        mask, d, result, r = 0x0FFFFF, {'A' : 0x0, 'T' : 0x1, 'G' : 0x2, 'C' : 0x3}, [], {}
        key = d[s[0]]
        for index in range(1, 10):
            key = key * 4 + d[s[index]]
        r[key] = True
        for index in range(10, len(s)):
            key = (key * 4 + d[s[index]]) & mask
            if key in r and r[key]:
                result.append(s[index - 9 : index + 1])
                r[key] = False
            elif key not in r:
                r[key] = True
        return result

if __name__ == '__main__':
    pass