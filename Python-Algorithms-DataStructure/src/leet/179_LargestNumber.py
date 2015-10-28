'''
Created on 2015-10-28
'''

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        : 12 comes before 121 since 12|121 > 121|12
        : This problem is particularly good for Python interview
        """
        class Key:
            def __init__(self, s, *args):
                self.s = s
            
            def __lt__(self, other):
                return (self.s + other.s) < (other.s + self.s)
                
            def __gt__(self, other):
                return (self.s + other.s) > (other.s + self.s)
            
            def __eq__(self, other):
                return (self.s + other.s) == (other.s + self.s)
        
            def __le__(self, other):
                return (self.s + other.s) <= (other.s + self.s)
        
            def __ge__(self, other):
                return (self.s + other.s) >= (other.s + self.s)

            def __ne__(self, other):
                return (self.s + other.s) != (other.s + self.s)

        result, index = ''.join(sorted([str(n) for n in nums], key=Key, reverse=True)), 0
        # Take care of the preceding zeros
        while index < len(result) and result[index] == '0':
            index += 1
        return '0' if index == len(result) else result[index:]

if __name__ == '__main__':
    pass