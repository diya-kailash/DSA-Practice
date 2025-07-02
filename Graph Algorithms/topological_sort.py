# Topological Sort using DFS - Directed Acyclic Graph (DAG)
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}
def topological_sort(graph):
    visited = set()
    stack = []
    def dfs(node):
        if node not in visited:
            visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]  

print("Topological Sort:", topological_sort(graph))

