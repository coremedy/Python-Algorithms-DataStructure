'''
Created on 2015-07-24
'''

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        s_length = len(s)
        table = [[False] for dummy_index in range(s_length)]
        for index in range(s_length):
            for start_index in range(index, -1, -1):
                if start_index:
                    if (table[start_index - 1][0]) and (s[start_index : index + 1] in wordDict):
                        table[index][0] = True
                        table[index].append(start_index - 1) 
                else:
                    if s[start_index : index + 1] in wordDict:
                        table[index][0] = True
                        table[index].append(-1)
        if table[s_length - 1][0]:
            result = []
            self.back_track(table, s, s_length - 1, [], result)
            return result
        else:
            return []
        
    def back_track(self, table, s, index, stack, result):
        # Baseline
        if index == -1:
            # process result
            result.append(" ".join(reversed(stack)))
        else:
            for i in range(1, len(table[index])):
                # Track
                stack.append(s[table[index][i] + 1 : index + 1])
                self.back_track(table, s, table[index][i], stack, result)
                # Back
                stack.pop()

if __name__ == '__main__':
    pass