'''
Created on 2015-10-06
'''

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x, y = min(C, G) - max(A, E), min(D, H) - max(B, F)
        return (D - B) * (C - A) + (H - F) * (G - E) - (0 if x <= 0 or y <= 0 else x * y)

if __name__ == '__main__':
    pass