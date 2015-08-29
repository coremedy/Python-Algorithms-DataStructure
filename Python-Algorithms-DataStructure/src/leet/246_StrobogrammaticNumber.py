'''
Created on 2015-08-29
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapper = {'0' : '0', '1' : '1', '8' : '8', '6' : '9', '9' : '6'}
        result = []
        for ch in reversed(num):
            if ch not in mapper:
                return False
            result.append(mapper[ch])
        return ''.join(result) == num
    
if __name__ == '__main__':
    pass