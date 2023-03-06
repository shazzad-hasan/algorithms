def bfs(graph, start):

    visited = [start]
    queue = [start]

    while queue:
        vertix = queue.pop(0)

        for v in graph[vertix]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
        
    return visited


# test 1
g1 = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
print(bfs(g1, "A"))

# test 2
g2 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
print(bfs(g2, "A"))
