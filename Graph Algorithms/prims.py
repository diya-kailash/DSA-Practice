# Prim's Algorithm 
# Time Complexity: O((V + E) * log V)
# Space Complexity: O(V + E)
# When to Use: Use Prim’s algorithm to find the Minimum Spanning Tree (MST) of a weighted, connected, undirected graph, minimizing the total edge weight.

import heapq
graph = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (2, 3), (3, 4)],
    2: [(0, 5), (1, 3), (3, 6), (4, 2)],
    3: [(1, 4), (2, 6), (5, 1)],
    4: [(2, 2), (5, 7), (6, 3)],
    5: [(3, 1), (4, 7), (6, 8)],
    6: [(4, 3), (5, 8)]
}
def prims(start):
    min_heap = []
    mst = []
    total_weight = 0
    visited = [False] * len(graph)
    heapq.heappush(min_heap, (0, start, -1))
    while min_heap:
        wt, u, parent = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = True
            if parent != -1:
                mst.append((parent, u))
                total_weight += wt
            for v, wt in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (wt, v, u))
    return mst, total_weight

mst, total_weight = prims(0)
print("MST:", mst)
print("Total Weight:", total_weight)