# adjacency list representation of the graph
def dfs_list(graph, start):
    stack = [start]
    visited = set()
    visited.add(start)
    traversal_path = []
    while stack:
        current = stack.pop()
        traversal_path.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    print("DFS Traversal Path:", traversal_path)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_list(graph, 'A')


# adjacency matrix representation of the graph
def dfs_matrix(adj_matrix, start):
    stack = [start]
    visited = [False] * len(adj_matrix)
    visited[start] = True
    traversal_path = []
    while stack:
        current = stack.pop()
        traversal_path.append(current)
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[current][neighbor] and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    print("DFS Traversal Path:", traversal_path)
    return traversal_path

adj_matrix = [
    [0,1,1,0,0,0],  
    [0,0,0,1,1,0],  
    [0,0,0,0,0,1],  
    [0,0,0,0,0,0],  
    [0,0,0,0,0,1],  
    [0,0,0,0,0,0],  
]
dfs_matrix(adj_matrix, 0)