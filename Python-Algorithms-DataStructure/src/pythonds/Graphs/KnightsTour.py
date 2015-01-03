'''
Created on 2015-01-05
Code coming from: http://interactivepython.org/runestone/static/pythonds/Graphs/BuildingtheKnightsTourGraph.html
'''

from pythonds.Graphs.Graph import Graph

def posToNodeID(row, col, boardSize):
    return row * boardSize + col

def genLegalMoves(row, col, boardSize):
    legalMoves = []
    offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for o in offsets:
        newRow = row + o[0]
        newCol = col + o[1]
        if (newRow >= 0) and (newRow < boardSize) and (newCol >= 0) and (newCol < boardSize):
            legalMoves.append((newRow, newCol))
    return legalMoves

def genKnightGraph(boardSize):
    knightGraph = Graph()
    for row in range(boardSize):
        for col in range(boardSize):
            currentNodeID = posToNodeID(row, col, boardSize)
            # a list of tuples
            legalMoves = genLegalMoves(row, col, boardSize)
            for t in legalMoves:
                targetNodeID = posToNodeID(t[0], t[1], boardSize)
                knightGraph.addEdge(currentNodeID, targetNodeID)
    return knightGraph

if __name__ == '__main__':
    path_recorder = []
    g = genKnightGraph(8)
    if g.getVertex(0).backtrack_knightTour(0, 7, path_recorder):
        print(list(map(lambda v: v.getId(), path_recorder)))
    g.getVertex(0).dfs_colorBack_postKnightTour()