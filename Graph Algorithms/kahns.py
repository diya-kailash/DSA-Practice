# Kahn's Algorithm for Topological Sort using BFS
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# When to Use: Use Kahn’s Algorithm for topological sorting of Directed Acyclic Graphs (DAGs) when you need a queue-based, non-recursive approach to handle task scheduling, dependency resolution, and build ordering.

from collections import deque, defaultdict
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}
def kahns(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    queue = deque([node for node in graph if indegree[node] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)    
    return order

print(kahns(graph))
