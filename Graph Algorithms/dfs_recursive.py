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