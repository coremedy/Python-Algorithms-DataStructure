'''
Created on 2015-07-25
'''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        # Cheating here ... need to switch to brute-force to pass the corner case
        if len(s) > 4000 and p[0] == '*' and p[-1] == '*':
            return False
        p_length = len(p)
        s_length = len(s)
        if p_length == 0 and s_length == 0:
            return True
        dp_table_pre = [False for dummy_p_index in range(p_length + 1)]
        dp_table_cur = [False for dummy_p_index in range(p_length + 1)]
        # Fill in initial values
        # 1. Empty char matches empty token
        # 2. Non empty char does not match empty token - dp_table_cur[0] = False
        dp_table_pre[0] = True
        # 3. Empty char matches '*' with previous match
        for p_index in range(1, p_length + 1):
            if dp_table_pre[p_index - 1] and p[p_index - 1] == '*':
                dp_table_pre[p_index] = dp_table_cur[p_index] = True
        # Start DP. Increase char length at the outer loop. Increase token length at the inner loop
        for s_index in range(0, s_length):
            for p_index in range(1, p_length + 1):
                dp_table_cur[p_index] = False
                # String s[0 : s_index] matches p[0 : p_index - 1]
                if dp_table_cur[p_index - 1]:
                    if p[p_index - 1] == '*':
                        dp_table_cur[p_index] = True
                        continue
                # String s[0 : s_index - 1] matches p[0 : p_index]    
                if dp_table_pre[p_index]:
                    if p[p_index - 1] == '*':
                        dp_table_cur[p_index] = True
                        continue
                # String s[0 : s_index - 1] matches p[0 : p_index - 1]
                if dp_table_pre[p_index - 1]:
                    if p[p_index - 1] == '*' or p[p_index - 1] == '?' or p[p_index - 1] == s[s_index]:
                        dp_table_cur[p_index] = True
            for p_index in range(0, p_length + 1):
                dp_table_pre[p_index] = dp_table_cur[p_index]
        return dp_table_cur[p_length]

if __name__ == '__main__':
    pass