from collections import deque

def bfs(graph, start_node):
    visited = set()  # Track visited nodes
    queue = deque([start_node])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue the first element

        if node not in visited:
            print(node, end=" ")  # Output the visited node
            visited.add(node)  # Mark the node as visited

            # Enqueue unvisited neighbors
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],  # Cycle: 'A' can be revisited from 'E'
    'F': []
}

bfs(graph, 'A')
