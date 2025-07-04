# Dijkstra's Algorithm 
# Time Complexity: O((V + E) * log V) 
# Space Complexity: O(V)
# When to Use: Use Dijkstra’s algorithm to find the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.

import heapq
graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(4, 3)],
    3: [(5, 1)],
    4: [(3, 2), (5, 5)],
    5: []
}
def dijkstras(start):
    min_heap = []
    distance = [float('inf')] * len(graph)
    distance[start] = 0
    heapq.heappush(min_heap, (0, start))
    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)
        for v, wt in graph[u]:
            if curr_dist + wt < distance[v]:
                distance[v] = curr_dist + wt
                heapq.heappush(min_heap, (distance[v], v))
    return distance

print(dijkstras(0))
