from queue import Queue 
from graph import * 

def breadth_first_search(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.num_vertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue 

        print("Visit: ", vertex)
        visited[vertex] = 1

        for v in graph.getAdjacentVertices(vertex):
            if visited[v] != 1:
                queue.put(v)


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

    breadth_first_search(g, 0)

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

    breadth_first_search(g, 0)

if __name__ == "__main__":
    main()

