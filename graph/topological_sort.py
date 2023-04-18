def find_indegree(graph):
    # construct a dict mapping nodes to their indegrees
    indegree = {node: 0 for node in graph}

    # count the in-degree of each node
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1 
    return indegree 

def topological_sort(graph):
    # find each node's indegree
    indegree = find_indegree(graph)

    # track nodes with no 0 in-degree
    nodes_with_indegree_0 = [node for node in graph if indegree[node] == 0]
    
    topological_ordering = []
    # keep looping until there aren't any more nodes with 0 indegree
    while len(nodes_with_indegree_0) > 0:
        # add one of those nodes to the topological ordering
        node = nodes_with_indegree_0.pop()
        topological_ordering.append(node)

        # subtract 1 from the indegree of that node's neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1 
            # If a node's in-degree drops to 0
            if indegree[neighbor] == 0:
                nodes_with_indegree_0.append(neighbor)
    
    # If any nodes remain unprocessed, then there must be a cycle
    if len(topological_ordering) == len(graph):
        return topological_ordering 
    else:
        raise Exception("Graph with cycle doesn't have a topological ordering!")
    
if __name__ == "__main__":
    g1 = {
        "A": ["C", "D"],
        "B": ["C", "E"],
        "C": ["D"],
        "D": [],
        "E": ["A", "C"]
    }
    print(topological_sort(g1))
    
    print()

    g2 = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["B"]
    }
    print(topological_sort(g2))
