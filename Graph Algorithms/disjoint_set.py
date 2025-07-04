# Union-Find (Disjoint Set Union - DSU) with Path Compression and Union by Rank
# Time Complexity: O(α(N)) per operation  # α(N) is the inverse Ackermann function, nearly constant time
# Space Complexity: O(N)
# When to Use: Use Union-Find to efficiently manage disjoint sets, commonly used in Kruskal's algorithm, cycle detection in graphs, and dynamic connectivity problems.

n = 7 
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

edges = [(0, 1), (1, 2), (3, 4), (5, 6), (2, 4)]
for u, v in edges:
    union(u, v)
print("Parent array after unions:", parent)

# Check if some nodes are in the same set
def same_set(u, v):
    return find_parent(u) == find_parent(v)
print("Are 0 and 4 connected?", same_set(0, 4))  # True
print("Are 0 and 6 connected?", same_set(0, 6))  # False
print("Are 5 and 6 connected?", same_set(5, 6))  # True


