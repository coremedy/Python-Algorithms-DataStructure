'''
Created on 2015-11-01
'''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edge_set, vertex_set = set(), set()
        for index in range(len(words) - 1):
            vertex_set, tup = vertex_set | set(list(words[index])), self.getEdge(words[index], words[index + 1])
            if tup:
                edge_set.add(tup)
        vertex_set, self.d = vertex_set | set(list(words[-1])), dict()
        for v in vertex_set:
            self.d[v] = [False]
        for e in edge_set:
            self.d[e[0]].append(e[1])
        self.result, self.bookmark, self.valid = [], set(), True
        for v in vertex_set:
            if not self.valid:
                return ''
            elif not self.d[v][0]:
                self.dfs(v)
        return ''.join(reversed(self.result))
        
    def dfs(self, node):
        self.d[node][0] = True
        for index in range(1, len(self.d[node])):
            if not self.d[self.d[node][index]][0]:
                # cycle detection
                self.bookmark.add(node)
                self.dfs(self.d[node][index])
                if not self.valid:
                    return
                self.bookmark.remove(node)
            elif self.d[node][index] in self.bookmark:
                self.valid = False
                return
        # post-order for topo sort
        self.result.append(node)
        
    def getEdge(self, w1, w2):
        length, index = min(len(w1), len(w2)), 0
        while index < length:
            if w1[index] != w2[index]:
                break
            index += 1
        if index == length:
            return None
        else:
            return (w1[index], w2[index])

if __name__ == '__main__':
    pass