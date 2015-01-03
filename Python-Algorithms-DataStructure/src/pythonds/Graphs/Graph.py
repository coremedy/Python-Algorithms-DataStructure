'''
Created on 2014-12-31
Code coming from: http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
'''

from pythonds.Graphs.Vertex import Vertex
from adt.queues.queue import Queue

class Graph(object):
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0
        
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
    
    # this can only do BFS on the nodes connected to self (the current connected component)
    def bfs_undirected(self, curr):
        # preparation
        vertexQueue = Queue()
        curr.setColor('gray')
        vertexQueue.enqueue(curr)
        # breath-first
        while not vertexQueue.isEmpty():
            currentVertex = vertexQueue.dequeue()
            for neighbour in currentVertex.getConnections():
                if neighbour.getColor() == 'white':
                    neighbour.setColor('gray')
                    neighbour.setDistance(currentVertex.getDistance() + 1)
                    neighbour.setPred(currentVertex)
                    vertexQueue.enqueue(neighbour)
            currentVertex.setColor('black')
        # get the color back
        curr.setColor('gray')
        vertexQueue.enqueue(curr)
        while not vertexQueue.isEmpty():
            currentVertex = vertexQueue.dequeue()
            for neighbour in currentVertex.getConnections():
                if neighbour.getColor() == 'black':
                    neighbour.setColor('gray')
                    vertexQueue.enqueue(neighbour)
            currentVertex.setColor('white')
            
    '''
    Some explanation:
    When we use pure dfs, we will get a TREE from the graph.
    However, if you need to get a special form of TREE (he deepest depth first TREE, like a segment), pure dfs is not feasible and you need to backtrack.
    In Knight Tour Problem, you need to get a PATH containing all vertices and every vertex is visited exactly once.
    This is actually a new permutation of the vertices, satisfying certain relations.
    So backtrack here!
    '''
    # this can only do DFS on the nodes connected to self (the current connected component)
    def backtrack_knightTour(self, curr, current_path_length, path_length_limit, path_recorder):
        done = False
        if current_path_length == path_length_limit:
            # we are done
            curr.setColor('gray')
            path_recorder.append(curr)
            done = True
        else:
            curr.setColor('gray')
            path_recorder.append(curr)            
            for neighbour in orderByAvail(curr):
                if neighbour.getColor() == 'white':
                    # you need to use the result of recursive call to determine whether to backtrack or not
                    done = self.backtrack_knightTour(neighbour, current_path_length + 1, path_length_limit, path_recorder)
                if done:
                    break
            if not done:
                # backtrack
                curr.setColor('white')
                path_recorder.pop()
        return done
    
    # This can do DFS on all connected components
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.__dfs_visit(aVertex)

    def __dfs_visit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.__dfs_visit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

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

# heuristic searches
# THIS REALLY MAKES A DIFFERENCE!!!
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

if __name__ == '__main__':
    g = buildWordLadderGraph("C:\\test.txt")
    g.bfs_undirected(g.getVertex('fool'))
    print(g.getVertex('sage').getDistance())
    g.dfs()