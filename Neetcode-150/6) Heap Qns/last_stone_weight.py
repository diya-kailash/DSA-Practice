# Last Stone Weight
# Overall Time Complexity: O(n log n)
# Overall Space Complexity: O(n)
# Hint: Use a max-heap (by inserting negative values) to repeatedly smash two heaviest stones

import heapq
def lastStoneWeight(stones):
    heap = []
    for x in stones:
        heapq.heappush(heap, -x)  
    while len(heap) > 1:
        s1 = -heapq.heappop(heap)  
        s2 = -heapq.heappop(heap) 
        if s1 < s2:
            heapq.heappush(heap, -(s2 - s1))  
        elif s2 < s1:
            heapq.heappush(heap, -(s1 - s2))  
    return -heap[0] if heap else 0

# Time Complexity:
# - Building the heap from n elements: O(n log n)
# - Each pop/push operation in the loop: O(log n)
# - In worst case, while loop runs n-1 times: O(n)
# Space Complexity:
# - Heap stores up to n elements: O(n)
# - No additional space used



