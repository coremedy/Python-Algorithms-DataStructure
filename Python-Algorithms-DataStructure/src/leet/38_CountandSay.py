'''
Created on 2015-10-14
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        result, i = '1', 1, 
        while i < n:
            tmp, count, cur = '', 0, ''
            for ch in result:
                if ch == cur:
                    count += 1
                else:
                    tmp, cur, count = tmp if count == 0 else (tmp + str(count) + cur), ch, 1
            result, i = tmp + str(count) + cur, i + 1
        return result

if __name__ == '__main__':
    pass