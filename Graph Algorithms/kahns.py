# Kahn's Algorithm - Topological Sort using BFS - Directed Acyclic Graph (DAG)
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
