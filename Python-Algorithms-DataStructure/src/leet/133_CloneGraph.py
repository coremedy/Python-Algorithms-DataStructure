'''
Created on 2015-08-01
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return
        recorder = dict()
        return self.BFS(node, recorder)
        
    def DFS(self, node, recorder):
        # Baseline and repetition elimination
        if node in recorder:
            return recorder[node]
        # DFS
        node_clone = UndirectedGraphNode(node.label)
        recorder[node] = node_clone
        for neighbour in node.neighbors:
            node_clone.neighbors.append(self.DFS(neighbour, recorder))
        return node_clone
        
    def BFS(self, node, recorder):
        nodes = [(node, None, 0)]
        nodes_start = 0
        nodes_stop = 1
        while True:
            count = 0
            for index in range(nodes_start, nodes_stop):
                node_clone = None
                if nodes[index][0] not in recorder:
                    node_clone = UndirectedGraphNode(nodes[index][0].label)
                    recorder[nodes[index][0]] = node_clone
                    for i in range(len(nodes[index][0].neighbors)):
                        if nodes[index][0].neighbors[i] in recorder:
                            node_clone.neighbors.append(recorder[nodes[index][0].neighbors[i]])
                        else:
                            node_clone.neighbors.append(nodes[index][0].neighbors[i])
                            nodes.append((nodes[index][0].neighbors[i], node_clone, i))
                            count += 1
                else:
                    node_clone = recorder[nodes[index][0]]
                if nodes[index][1] is not None:
                    nodes[index][1].neighbors[nodes[index][2]] = node_clone
            if count == 0:
                break
            nodes_start, nodes_stop = nodes_stop, nodes_stop + count
        return recorder[node]

if __name__ == '__main__':
    pass