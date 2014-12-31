'''
Created on 2014-12-31
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

if __name__ == '__main__':
    pass