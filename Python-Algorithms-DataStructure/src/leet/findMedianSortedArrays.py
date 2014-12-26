'''
Created on 2014-12-26
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length_of_A = len(A)
        length_of_B = len(B)
        k = (length_of_A + length_of_B) / 2
        # total length is odd
        if (length_of_A + length_of_B) % 2 == 1:
            return self.__get_k(A, B, k + 1)
        # total length is even
        else:
            return 0.5 * (self.__get_k(A, B, k) + self.__get_k(A, B, k + 1))
    
    def __get_k(self, A, B, k):
        length_of_A = len(A)
        length_of_B = len(B)
        # make sure that the length of A will approach zero first
        if length_of_A > length_of_B:
            return self.__get_k(B, A, k)
        # baseline: A becomes zero
        if not length_of_A:
            return B[k - 1]
        # baseline: k is one
        if k == 1:
            return min(A[0], B[0])
        # Offset or K does not equal index !
        offset_A = min(k / 2, length_of_A)
        offset_B = k - offset_A
        # A[0] ... A[offset_A - 1] , A[offset_A] ... A[length_of_A - 1]
        # B[0] ... B[offset_B - 1] , B[offset_B] ... B[length_of_B - 1]
        # if A[offset_A - 1] <= B[offset_B - 1]
        # there are at least (length_of_A - offset_A) + (length_of_B - (k - offset_A) + 1) = length_of_A + length_of_B - k + 1
        # coming after A[offset_A - 1], so k should belong to this part and k cannot fall in the range of A[0] ... A[offset_A - 1]
        # The 1 in (length_of_B - (k - offset_A) + 1) represents B[offset_B - 1]
        if A[offset_A - 1] <= B[offset_B - 1]:
            return self.__get_k(A[offset_A:], B, k - offset_A)
        # similar reason
        else:
            return self.__get_k(A, B[offset_B:], k - offset_B)

if __name__ == '__main__':
    pass