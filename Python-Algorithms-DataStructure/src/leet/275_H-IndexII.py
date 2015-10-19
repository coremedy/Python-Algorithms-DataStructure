'''
Created on 2015-10-19
Count    citation
   ¡Á        &
    ¡Á     &
      ¡Á&
    &   ¡Á
The cross point is the h value
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        elif len(citations) == 1:
            return min(1, citations[0])
        else:
            n, beg, end = len(citations), 0, len(citations) - 1
            while beg <= end:
                mid = (beg + end) // 2
                if n - mid == citations[mid]:
                    return n - mid
                elif n - mid > citations[mid]:
                    beg = mid + 1
                else:
                    end = mid - 1
            return n - beg

if __name__ == '__main__':
    pass