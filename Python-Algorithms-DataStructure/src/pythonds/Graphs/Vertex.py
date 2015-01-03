'''
Created on 2015-01-03
Code coming from: http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
'''

from adt.queues.queue import Queue

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.pred = None
        self.dist = 0
    
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setPred(self, pred):
        self.pred = pred
        
    def getPred(self):
        return self.pred
    
    def setDistance(self, dist):
        self.dist = dist
        
    def getDistance(self):
        return self.dist
    
    def bfs_undirected(self):
        # preparation
        vertexQueue = Queue()
        self.setColor('gray')
        vertexQueue.enqueue(self)
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
        self.setColor('gray')
        vertexQueue.enqueue(self)
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
    However, if you need to get a special form of TREE (the special TREE looks like a segment and it is
    actually a PATH containing all vertices, exactly ONCE), pure dfs is not feasible and you need to backtrack.
    In Knight Tour Problem, you need to get a PATH containing all vertices and every vertex is visited exactly once.
    This is actually a new permutation of the vertices, satisfying certain relations.
    So backtrack here!
    '''
    def backtrack_knightTour(self, current_path_length, path_length_limit, path_recorder):
        done = False
        if current_path_length == path_length_limit:
            # we are done
            self.setColor('gray')
            path_recorder.append(self)
            done = True
        else:
            self.setColor('gray')
            path_recorder.append(self)            
            for neighbour in self.getConnections():
                if neighbour.getColor() == 'white':
                    # you need to use the result of recursive call to determine whether to backtrack or not
                    done = neighbour.backtrack_knightTour(current_path_length + 1, path_length_limit, path_recorder)
                if done:
                    break
            if not done:
                # backtrack
                self.setColor('white')
                path_recorder.pop()
        return done
    
    def dfs_colorBack_postKnightTour(self):
        self.setColor('white')
        for neighbour in self.getConnections():
            if neighbour.getColor() != 'white':
                neighbour.dfs_colorBack_postKnightTour()

if __name__ == '__main__':
    pass