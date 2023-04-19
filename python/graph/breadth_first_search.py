def bfs(graph, start):
    visited, queue = [start], [start]
    
    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")

        for v in graph[vertex]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

def main():
    """
             A
          /     \
         B       C
       /   \     | \
      D     E    F   G
            |
            H
    """
    g1 = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["B", "H"],
        "F": ["C"],
        "G": ["C"],
        "H": ["E"]
    }
    bfs(g1, "A")
    
    print()

    """ 
          A
        /   \
       B     C
      / \     \
     D   E --- F
    """
    g2 = {
        'A' : ['B','C'],
        'B' : ['A', 'D', 'E'],
        'C' : ['A', 'F'],
        'D' : ['B'],
        'E' : ['B', 'F'],
        'F' : ['C', 'E']
    }
    bfs(g2, "A")

if __name__ == "__main__":
    main()