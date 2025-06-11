# K Closest Points to Origin
# Overall Time Complexity: O(n log k)
# Overall Space Complexity: O(k)
# Hint: Use a max-heap of size k to maintain the k closest points by Euclidean distance

import heapq, math
def kClosest(points, k):
    heap = []
    output = []
    for x, y in points:
        d = math.sqrt(x**2 + y**2)              
        heapq.heappush(heap, (-d, [x, y]))       
        if len(heap) > k:
            heapq.heappop(heap)               
    for i in range(k):
        d, point = heapq.heappop(heap)          
        output.append(point)
    return output

# Time Complexity:
# - For each of the n points:
#   - Compute distance: O(1)
#   - Push to heap of size at most k: O(log k)
#   - Optional pop if heap exceeds size k: O(log k)
#   - Total for loop: O(n log k)
# - Extract k points from heap: O(k log k)
# - Total: O(n log k + k log k) which simplifies to O(n log k) since n >= k
# Space Complexity:
# - Heap stores at most k elements: O(k)
# - Output list stores k elements: O(k)

points = [[0,2],[2,2]]
k = 1
print(kClosest(points, k))  # Output: [[0, 2]]
points = [[0,2],[2,0],[2,2]]
k = 2
print(kClosest(points, k))  # Output: [[0, 2], [2, 0]]
