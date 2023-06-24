from graph import *

def deapth_first_search(graph, visited, current=0):
    if visited[current] == 1:
        return 
    
    print("Visit: ", current)
    visited[current] = 1
    for v in graph.getAdjacentVertices(current):
        deapth_first_search(graph, visited, v)

def main():
    """
        0
        |
        1 
      /   \
     2     5
   / | \    \
 7   4--3----6
              \
               8
    """
    
    g = AdjacencyMatrixGraph(9)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 7)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(1, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 3)
    g.addEdge(3, 4)
    g.addEdge(6, 8)

    visited = np.zeros(g.num_vertices)
    deapth_first_search(g, visited, 0)

    print()

    g = AdjacencyMatrixGraph(9, directed=True)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 7)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(1, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 3)
    g.addEdge(3, 4)
    g.addEdge(6, 8)

    visited = np.zeros(g.num_vertices)
    deapth_first_search(g, visited, 0)

if __name__=="__main__":
    main()