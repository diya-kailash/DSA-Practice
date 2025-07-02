graph = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (2, 3), (3, 4)],
    2: [(0, 5), (1, 3), (3, 6), (4, 2)],
    3: [(1, 4), (2, 6), (5, 1)],
    4: [(2, 2), (5, 7), (6, 3)],
    5: [(3, 1), (4, 7), (6, 8)],
    6: [(4, 3), (5, 8)]
}
edges = []
added = set()
for u in graph:
    for v, wt in graph[u]:
        if (v, u) not in added: 
            edges.append((wt, u, v))
            added.add((u, v))
edges.sort()
n = len(graph)
parent = [i for i in range(n)]
rank = [0] * n
def find_parent(u):
    if parent[u] != u:
        parent[u] = find_parent(parent[u])
    return parent[u]
def union(u, v):
    pu = find_parent(u)
    pv = find_parent(v)
    if pu != pv:
        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pv] < rank[pu]:
            parent[pv] = pu
        else:
            parent[pu] = pv
            rank[pv] += 1
        return True
    return False
def kruskals():
    mst = []
    total_weight = 0
    for wt, u, v in edges:
        if union(u, v):
            mst.append((u, v))
            total_weight += wt
    return mst, total_weight

mst, total_weight = kruskals()
print("MST:", mst)
print("Total Weight:", total_weight)
