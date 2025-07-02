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
        curr_dist, current = heapq.heappop(min_heap)
        for neighbor, weight in graph[current]:
            if curr_dist + weight < distance[neighbor]:
                distance[neighbor] = curr_dist + weight
                heapq.heappush(min_heap, (distance[neighbor], neighbor))
    return distance
print(dijkstras(0))
