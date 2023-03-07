class Vertex:
    def __init__(self, key):
        self.id = key 
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight 

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id 
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr] 
    
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0 

    def addVertex(self, key):   # O(1)
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex 
        return newVertex 
    
    def getVertex(self, key):   # O(1)
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None 
        
        # return self.vertexList.get(key)

    def __contains__(self, key):    # O(1)
        return key in self.vertexList
    
    def addEdge(self, f, t, w=0):   # O(1)
        if f not in self.vertexList:
            new_vertex = self.addVertex(f)
        if t not in self.vertexList:
            new_vertex = self.addVertex(t)
        self.vertexList

        self.vertexList[f].addNeighbour(self.vertexList[t], w)

    def getVertices(self):  # O(1)
        return self.vertexList.keys()
    
    def getCount(self): # O(1)
        return self.numVertices
    
    def __iter__(self):
        return iter(self.vertexList.values())
    

def main():
    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.addEdge(0, 1, 5) 
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("( %s, %s )" % (v.getId(), w.getId()))

if __name__ == "__main__":
    main()
