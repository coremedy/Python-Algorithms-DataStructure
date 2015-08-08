'''
Created on 2015-08-07
'''

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
            if len(token) > 0 and token != '.':
                if token == '..':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(token)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    pass