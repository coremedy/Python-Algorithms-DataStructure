'''
Created on 2015-10-14
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        prefix, index = '', 0
        while True:
            cur = '' if index == len(strs[0]) else strs[0][index]
            if len(cur) == 0:
                return prefix
            for s in strs[1:]:
                if index == len(s) or cur != s[index]:
                    return prefix
            index, prefix = index + 1, prefix + cur
        return prefix

if __name__ == '__main__':
    pass