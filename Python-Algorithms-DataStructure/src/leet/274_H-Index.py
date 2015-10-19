'''
Created on 2015-10-19
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        : citations                                                         = [3, 0, 6, 1, 5]
        : arrange it to                                                       [6, 5, 3, 1, 0]
        : index (count, the number of papers having value no less than ....)   1  2  3  4  5
        : min(index, val)                                                      1  2  3  1  0
        : max(min(index, val)) -> 3 is the largest
        : so: if there are N papers, the largest value cannot be greater than N
        : that's why we use citation_count = [0] * (n + 1) to record the count for citation value from 1 to N
        : for those having citation value > N, just add 1 to the count of N
        : For the range of citation values from N to 1, let's check the count (or index)
        : Since the largest citation value cannot be greater than N
        : if the count is greater than or equal to current val, than means min(index, val) = val
        : Since the values are ordered in decending order, val is the right answer
        """
        n = len(citations)
        citation_count = [0] * (n + 1)
        for c in citations:
            citation_count[[c, n][c > n]] += 1
        s = 0
        for i in range(n, 0, -1):
            if s + citation_count[i] >= i:
                return i
            s += citation_count[i]
        return 0

if __name__ == '__main__':
    pass