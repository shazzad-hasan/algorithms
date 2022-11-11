def dfs(graph, start):
    
    visited = []
    stack = [start]

    while stack:
        vertix = stack.pop()
        if vertix not in visited:
            visited.append(vertix)
            
        if vertix not in graph:
            continue

        for v in reversed(graph[vertix]):
            if v not in visited:
                stack.append(v)
        
    return visited 

g1 = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

print(dfs(g1, "A"))

g2 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
print(dfs(g2, "A"))

g3 = {
    "A":["B", "C", "D"],
    "B":["E"],
    "C":["F", "G"],
    "D":["H"],
    "E":["I"],
    "F":["J"]
}
print(dfs(g3, "A"))

g4 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
print(dfs(g4, "A"))