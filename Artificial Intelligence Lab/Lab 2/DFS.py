def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set for tracking

    visited.add(node)  # Mark the node as visited
    print(node, end=" ")  # Output the node

    # Explore neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit unvisited neighbors

# Example graph (adjacency list) with potential cycles
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],  # Cycle: 'A' can be revisited from 'E'
    'F': []
}

# Start DFS from node 'A'
dfs(graph, 'A')
