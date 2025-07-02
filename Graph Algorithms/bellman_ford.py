graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(4, 3)],
    3: [(5, 1)],
    4: [(3, 2), (5, 5)],
    5: []
}
def bellman_ford(start):
    V = len(graph)
    distance = [float('inf')] * V
    distance[start] = 0
    # Relax edges (V - 1) times
    for i in range(V - 1):
        for u in graph:
            for v, wt in graph[u]:
                if distance[u] != float('inf') and distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
    # Detect negative weight cycles
    for u in graph:
        for v, wt in graph[u]:
            if distance[u] != float('inf') and distance[u] + wt < distance[v]:
                print("Graph contains a negative weight cycle")
                return
    return distance

print(bellman_ford(0))
