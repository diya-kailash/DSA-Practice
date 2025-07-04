# Depth-First Search (DFS) - Recursive
# Time Complexity: O(V + E)
# Space Complexity: O(V)  
# When to Use: Use recursive DFS for simpler, cleaner implementations when the graph is not too deep to avoid stack overflow; useful for connectivity checks, path finding, puzzle solving, and cycle detection.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
path = []
def dfs(node):
    if node not in visited:
        visited.add(node)
        path.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor)
dfs('A')
print(path)