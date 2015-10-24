'''
Created on 2015-10-24
Why traversing the tree again providing that you have the result of traversal in hand?!
'''

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        cur_root_val, path = -2147483648, []
        for n in preorder:
            if n < cur_root_val:
                return False
            while len(path) > 0 and n > path[-1]:
                cur_root_val = path[-1]
                path.pop()
            path.append(n)
        return True

    def verifyPreorder_constant_storage(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        cur_root_val, stack_top = -2147483648, -1
        for n in preorder:
            if n < cur_root_val:
                return False
            while stack_top >= 0 and n > preorder[stack_top]:
                cur_root_val = preorder[stack_top]
                stack_top -= 1
            preorder[stack_top + 1], stack_top = n, stack_top + 1
        return True

if __name__ == '__main__':
    pass