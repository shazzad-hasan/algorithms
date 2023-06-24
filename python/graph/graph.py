import abc
import numpy as np

# Base class representation of a graph with all the interface methods
class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices 
        self. directed = directed 

    @abc.abstractclassmethod
    def addEdge(self, v1, v2, weight):
        pass 

    @abc.abstractclassmethod 
    def getAdjacentVertices(self, v):
        pass 

    @abc.abstractclassmethod 
    def getIndegree(self, v):
        pass 

    @abc.abstractclassmethod 
    def getEdgeWeight(self, v1, v2):
        pass 

    @abc.abstractclassmethod 
    def display(self):
        pass 

# Representation of a graph as an adjacency matrix
class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

        self.matrix = np.zeros((num_vertices, num_vertices))

    def addEdge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds".format(v1, v2))
        if weight < 1:
            raise ValueError("An edge can't have weight < 1")
        
        self.matrix[v1][v2] = weight 

        # adjacency matrix of undirected graph is symmetric
        if self.directed == False:
            self.matrix[v2][v1] = weight 

    def getAdjacentVertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex {} is out of bound".format(v))
        
        return [i for i in range(self.num_vertices) if self.matrix[v][i] > 0]
        
    def getIndegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex {} is out of bound".format(v))
        indegree = 0 
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1 
        return indegree 
    
    def getEdgeWeight(self, v1, v2):
        return self.matrix[v1][v2]
    
    def display(self):
        for i in range(self.num_vertices):
            for v in self.getAdjacentVertices(i):
                print(i, "-->", v)

def main():

    """
          0
         / \
        1   2
             \
              3
    """
    g = AdjacencyMatrixGraph(4, directed=False)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)

    for i in range(4):
        print("Node {} adjacent to: {}".format(i, g.getAdjacentVertices(i)))

    for i in range(4):
        print("Indegree of node {} : {}".format( i, g.getIndegree(i)))

    for i in range(4):
        for j in g.getAdjacentVertices(i):
            print("edge: ({}, {}), weight: {}".format(i, j, g.getEdgeWeight(i,j)))

    g.display()

    print()

    g = AdjacencyMatrixGraph(4, directed=True)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)

    for i in range(4):
        print("Node {} adjacent to: {}".format(i, g.getAdjacentVertices(i)))

    for i in range(4):
        print("Indegree of node {} : {}".format( i, g.getIndegree(i)))

    for i in range(4):
        for j in g.getAdjacentVertices(i):
            print("edge: ({}, {}), weight: {}".format(i, j, g.getEdgeWeight(i,j)))

    g.display()

if __name__ == "__main__":
    main()

        