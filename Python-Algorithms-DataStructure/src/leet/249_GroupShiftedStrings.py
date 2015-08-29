'''
Created on 2015-08-29
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        strings.sort()
        d = dict()
        for s in strings:
            k = self.getHashKey(s)
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        result = []
        for k in d:
            result.append(d[k])
        return result

    def getHashKey(self, s):
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return '.'
        key = []
        for index in range(1, len(s)):
            key.append(str((ord(s[index]) - ord(s[index - 1]) + 26) % 26))
        return ''.join(key)

if __name__ == '__main__':
    pass