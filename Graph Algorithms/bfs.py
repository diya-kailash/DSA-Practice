# Breadth-First Search (BFS) 
# Time Complexity: O(V + E) 
# Space Complexity: O(V)
# When to Use: Use BFS when you need to find the shortest path in an unweighted graph, explore all nodes layer by layer, or check for connectivity in graphs.

from collections import deque

# adjacency list representation of the graph
def bfs_list(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    traversal_path = []
    while queue:
        current = queue.popleft()
        traversal_path.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print("BFS Traversal Path:", traversal_path)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs_list(graph, 'A')


# adjacency matrix representation of the graph
def bfs_matrix(adj_matrix, start):
    queue = deque([start])
    visited = [False] * len(adj_matrix)
    visited[start] = True
    traversal_path = []
    while queue:
        current = queue.popleft()
        traversal_path.append(current)
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[current][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    print("BFS Traversal Path:", traversal_path)
    return traversal_path

adj_matrix = [
    [0,1,1,0,0,0],  
    [0,0,0,1,1,0],  
    [0,0,0,0,0,1],  
    [0,0,0,0,0,0],  
    [0,0,0,0,0,1],  
    [0,0,0,0,0,0],  
]
bfs_matrix(adj_matrix, 0)

