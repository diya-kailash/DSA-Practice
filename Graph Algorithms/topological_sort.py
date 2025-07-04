# Topological Sort using DFS 
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# When to Use: Use Topological Sort on Directed Acyclic Graphs (DAGs) when you need to order tasks based on dependencies, such as in scheduling, build systems, and resolving symbol dependencies in compilers.

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

print(topological_sort(graph))

