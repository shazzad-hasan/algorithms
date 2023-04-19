def dfs_recursive(graph, node, visited=set()):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(graph, neighbour, visited)


def dfs_stack(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            print(vertex, end = " ")
        if vertex not in graph:
            continue
        for v in reversed(graph[vertex]):
            if v not in visited:
                stack.append(v)


def main():
    g1 = {
        "A": ["B", "C", "E"],
        "B": ["D", "F"],
        "C": ["G"],
        "D": ["B"],
        "E": ["A", "F"],
        "F": ["B", "E"],
        "G": ["C"],
    }
    print("Recursive DFS traversal:")
    dfs_recursive(g1, "A")

    print("\nStack-based DFS traversal:")
    dfs_stack(g1, "A")
    

if __name__ == "__main__":
    main()