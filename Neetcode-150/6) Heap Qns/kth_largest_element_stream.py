# Kth Largest Element in a Stream
# Overall Time Complexity: O(m log k) 
# Overall Space Complexity: O(k)
# Hint: Maintain a min-heap of size k to track the k largest elements

import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for x in nums:
            heapq.heappush(self.heap, x)      
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)     

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)       
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)        
        return self.heap[0]                  
    
# Time Complexity:
# - For __init__:
#   - Iterating over n elements: O(n)
#   - Each heap push and pop (if needed): O(log k)
#   - Total: O(n log k)
# - For add:
#   - heapq.heappush: O(log k)
#   - heapq.heappop (if size > k): O(log k)
#   - Total: O(log k) per add call and O(m log k) for m add calls
# Space Complexity:
# - Min-heap stores at most k elements: O(k)
# - No additional space used

k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))  # returns 4
print(kthLargest.add(5))  # returns 5
print(kthLargest.add(10)) # returns 5
print(kthLargest.add(9))  # returns 8