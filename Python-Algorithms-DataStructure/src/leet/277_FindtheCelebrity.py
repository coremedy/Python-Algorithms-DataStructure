'''
Created on 2015-11-04
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 0
        self.crowd = set([i for i in range(n)])
        while len(self.crowd) > 1:
            crowd_list = list(self.crowd)
            if len(crowd_list) % 2 == 1:
                self.filter(crowd_list.pop(), crowd_list[0])
            for i in range(len(crowd_list) // 2):
                self.filter(crowd_list[i], crowd_list[len(crowd_list) - 1 - i])
        if len(self.crowd) == 0:
            return -1
        e = self.crowd.pop()
        for i in range(n):
            if i != e and not (knows(i, e) and not knows(e, i)):
                return -1
        return e

    def filter(self, a, b):
        a_knows_b, b_knows_a = knows(a, b), knows(b, a)
        if not (a_knows_b and not b_knows_a):
            self.crowd.discard(b)
        if not (not a_knows_b and b_knows_a):
            self.crowd.discard(a)

if __name__ == '__main__':
    pass