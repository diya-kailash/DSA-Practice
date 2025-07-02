graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(4, 3)],
    3: [(5, 1)],
    4: [(3, 2), (5, 5)],
    5: []
}
def floyd_warshall():
    V = len(graph)
    INF = float('inf')
    dist = [[INF] * V for i in range(V)]
    for i in range(V):
        dist[i][i] = 0
    for u in graph:
        for v, wt in graph[u]:
            dist[u][v] = wt
    # Start the algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # Detect negative weight cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains a negative weight cycle")
            return
    return dist

result = floyd_warshall()
for row in result:
    print([x if x != float('inf') else -1 for x in row])
