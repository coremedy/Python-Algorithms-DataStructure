'''
Created on 2015-07-16
'''

# LIS, not KNAPSACK. Focus on s please!
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return False
        elif len(wordDict) == 1:
            if s == list(wordDict)[0]:
                return True
            else:
                return False
        else:
            result = [True]
            for upper_bound in range(1, len(s) + 1):
                result.append(False)
                for lower_bound in range(0, upper_bound):
                    if result[lower_bound] and s[lower_bound:upper_bound] in wordDict:
                        result[-1] = True
            return result[len(s)]

if __name__ == '__main__':
    pass