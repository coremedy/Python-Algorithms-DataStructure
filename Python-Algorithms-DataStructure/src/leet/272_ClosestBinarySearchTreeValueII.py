'''
Created on 2015-10-24
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.root, self.target, self.k, self.ps, self.ss = root, target, k, [], []
        self.find()
        result, pre, suc = [], None, None
        if self.ps[-1].val * 1.0 == target:
            result.append(self.ps[-1].val)
            pre, suc, k = self.getPredecessor(), self.getSuccessor(), k - 1
        elif self.ps[-1].val * 1.0 > target:
            suc, pre = self.ss[-1], self.getPredecessor()
        else:
            pre, suc = self.ps[-1], self.getSuccessor()
        while k > 0:
            if not pre and suc:
                result.append(suc.val)
                suc = self.getSuccessor()
            elif not suc and pre:
                result.append(pre.val)
                pre = self.getPredecessor()
            elif suc and pre:
                result.append(suc.val if abs(pre.val * 1.0 - target) > abs(suc.val * 1.0 - target) else pre.val)
                if abs(pre.val * 1.0 - target) > abs(suc.val * 1.0 - target):
                    suc = self.getSuccessor()
                else:
                    pre = self.getPredecessor()
            k = k - 1
        return result
        
    def find(self):
        next_node = self.root
        while next_node:
            self.ps.append(next_node)
            self.ss.append(next_node)
            next_node = None if self.target == next_node.val * 1.0 else (next_node.right if self.target > next_node.val * 1.0 else next_node.left)
    
    def getPredecessor(self):
        if not self.ps:
            return None
        if not self.ps[-1].left:
            current_node = self.ps.pop()
            while self.ps:
                if self.ps[-1].val > current_node.val:
                    self.ps.pop()
                else:
                    break
            if not self.ps:
                return None
        else:
            next_node = self.ps[-1].left
            while next_node:
                self.ps.append(next_node)
                next_node = next_node.right
        return self.ps[-1]

    def getSuccessor(self):
        if not self.ss:
            return None
        if not self.ss[-1].right:
            current_node = self.ss.pop()
            while self.ss:
                if self.ss[-1].val < current_node.val:
                    self.ss.pop()
                else:
                    break                    
            if not self.ss:
                return None
        else:
            next_node = self.ss[-1].right
            while next_node:
                self.ss.append(next_node)
                next_node = next_node.left
        return self.ss[-1]

if __name__ == '__main__':
    pass