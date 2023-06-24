# python implementation of graph representation using adjacency set

import abc

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

class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id 
        self.adjacency_set = set()

    def addEdge(self, v):
        if self.vertex_id == v:
            raise ValueError("The vertex %d can't be adjacent to itself." % v)
        
        self.adjacency_set.add(v)

    def getAdjacentVertices(self):
        return sorted(self.adjacency_set)
    
class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed = False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = [Node(i) for i in range(num_vertices)]

    def addEdge(self, v1, v2, weight = 1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices {} and {} are out of bounds.".format(v1, v2))
        
        # represent only unweighted graphs
        if weight != 1:
            raise ValueError("Edge weights of unweighted graphs can't be > 1")
        
        self.vertex_list[v1].addEdge(v2) 

        if self.directed == False:
            self.vertex_list[v2].addEdge(v1)
    
    def getAdjacentVertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertix %d is out of bound." % v)
        
        return self.vertex_list[v].getAdjacentVertices()
        
    def getIndegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertix %d is out of bound." % v)
        indegree = 0 
        for i in range(self.num_vertices):
            if v in self.getAdjacentVertices(i):
                indegree += 1 
        return indegree 
    
    def getEdgeWeight(self, v1, v2):
        return 1 
    
    def display(self):
        for i in range(self.num_vertices):
            for v in self.getAdjacentVertices(i):
                print(i, "-->", v )

def main():
    
    """
          0
         / \
        1   2
             \
              3
    """
    g = AdjacencySetGraph(4, directed=False)

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

    g = AdjacencySetGraph(4, directed=True)

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
