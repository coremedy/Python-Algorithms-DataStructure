'''
Created on 2015-10-18
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg, end = 1, n
        while True:
            mid = (beg + end) // 2
            if mid == beg:
                break
            if isBadVersion(mid):
                end = mid
            else:
                beg = mid
        return beg if isBadVersion(beg) else end

if __name__ == '__main__':
    pass