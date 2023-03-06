def dfs_recursive(graph, node, visited=set(), traversal = []):
    if node not in visited:
        # print(node, end = " ")
        visited.add(node)
        traversal.append(node)
        for neighbour in graph[node]:
            dfs_recursive(graph, neighbour, visited, traversal)
    return traversal


def dfs_stack(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertix = stack.pop()
        if vertix not in visited:
            visited.append(vertix)
            # print(vertix, end = " ")
        if vertix not in graph:
            continue
        for v in reversed(graph[vertix]):
            if v not in visited:
                stack.append(v)
    return visited 


def main():
    g1 = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    print("\nRecursive DFS:")
    print(dfs_recursive(g1, "A"))

    print("\nStack-based DFS:")
    print(dfs_stack(g1, "A"))
    print()

if __name__ == "__main__":
    main()