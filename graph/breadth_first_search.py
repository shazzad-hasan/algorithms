def bfs_traversal(graph, start):
    visited = [start]
    queue = [start]
    while queue:
        vertix = queue.pop(0)

        for v in graph[vertix]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

def main():
    g1 = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print(bfs_traversal(g1, "A"))

if __name__ == "__main__":
    main()