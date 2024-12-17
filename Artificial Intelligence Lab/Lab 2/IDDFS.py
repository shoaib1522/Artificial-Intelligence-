def dls(node, goal, graph, depth, visited):
    """Depth-Limited Search (DLS): A helper function for IDDFS"""
    if depth == 0 and node == goal:
        return True  # Goal found
    if depth > 0:
        visited.add(node)
        # Recur for all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(neighbor, goal, graph, depth - 1, visited):
                    return True
    return False

def iddfs(graph, start_node, goal):
    """IDDFS: Iterative Deepening DFS"""
    depth = 0
    while True:
        visited = set()  # Clear visited nodes for each new depth
        if dls(start_node, goal, graph, depth, visited):
            print(f"Goal '{goal}' found at depth {depth}")
            return
        depth += 1
        print(f"Depth {depth} completed, goal not found.")
        if depth > len(graph):  # This can be modified based on the graph structure
            print("Goal not found within depth limits.")
            return

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],  # Cycle: 'A' can be revisited from 'E'
    'F': []
}

# Start IDDFS from node 'A' to find 'F'
iddfs(graph, 'A', 'F')
