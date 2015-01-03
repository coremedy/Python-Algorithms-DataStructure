'''
Created on 2015-01-03
Code coming from: http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
'''

class Vertex:
        
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.pred = None
        self.dist = 0
        self.discovery_time = 0
        # The 'leaf' node has the smallest finish time while the 'root' node has the largest one
        # This can be used in topological sort
        # Those with large finish time come first and those with small one come last
        self.finish_time = 0
    
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
    
    def setDiscovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def setFinish(self, finish_time):
        self.finish_time = finish_time

if __name__ == '__main__':
    pass