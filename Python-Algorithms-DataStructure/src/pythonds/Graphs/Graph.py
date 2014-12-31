'''
Created on 2014-12-31
Code coming from: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
'''

from pythonds.Graphs.Vertex import Vertex

class Graph(object):
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        v = Vertex(key)
        self.vertList[key] = v
        self.numVertices += 1
        return v
    
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None
    
    def __contains__(self, key):
        return key in self.vertList
    
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def addEdge(self, begin, end, cost = 0):
        if begin not in self.vertList:
            self.addVertex(begin)
        if end not in self.vertList:
            self.addVertex(end)
        self.vertList[begin].addNeighbor(self.vertList[end], cost)

def buildWordLadderGraph(wordFile):
    d = {}
    g = Graph()
    # build relationship group
    with open(wordFile) as fh:
        for line in fh:
            word = line.rstrip()
            for i in range(len(word)):
                bucket_name = word[:i] + '_' + word[i + 1:]
                if bucket_name in d:
                    d[bucket_name].append(word)
                else:
                    d[bucket_name] = [word]
    # build graph
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

if __name__ == '__main__':
    g = buildWordLadderGraph("C:\\test.txt")
    g.getVertex('fool').bfs_undirected()
    print(g.getVertex('sage').getDistance())