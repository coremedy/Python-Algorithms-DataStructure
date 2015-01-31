'''
Created on 2015-02-01
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        curr_max, total_max = A[0], A[0]
        if len(A) > 1:
            index = 1
            while index < len(A):
                if (curr_max + A[index] >= A[index]):
                    curr_max = curr_max + A[index]
                else:
                    curr_max = A[index]
                if curr_max >= total_max:
                    total_max = curr_max
                index += 1
        return total_max

if __name__ == '__main__':
    pass