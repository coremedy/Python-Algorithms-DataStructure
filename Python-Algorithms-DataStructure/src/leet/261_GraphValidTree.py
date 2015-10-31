'''
Created on 2015-11-01
'''

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        self.table, self.used = [[] for dummy_i in range(n)], set()
        for e in edges:
            self.table[e[0]].append(e[1])
            self.table[e[1]].append(e[0])
        self.dfs(0)
        return len(self.used) == n
        
    def dfs(self, node):
        if node not in self.used:
            self.used.add(node)
            for nex in self.table[node]:
                self.dfs(nex)

if __name__ == '__main__':
    pass