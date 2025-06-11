# Task Scheduler
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(k), 
# Hint: Use a max-heap to always schedule the most frequent task and a queue to manage cooldowns

from collections import Counter
import heapq
def leastInterval(tasks, n):
    counts = Counter(tasks)                          
    heap = [-c for c in counts.values()]             
    heapq.heapify(heap)                              
    queue = []                                       
    cycles = 0
    while heap or queue:                            
        cycles += 1
        if heap:
            c = -heapq.heappop(heap)                 
            if c - 1 != 0:
                queue.append((-(c - 1), cycles + n))
        if queue and cycles == queue[0][1]:         
            heapq.heappush(heap, queue.pop(0)[0])    
    return cycles

# Time Complexity:
# - Counting task frequencies: O(n)
# - Heap operations (push/pop/heapify): O(log n)
# - Queue operations: Up to n entries, constant-time access: O(n)
# Space Complexity:
# - Heap stores up to k elements: O(k)
# - Queue stores up to k elements in cooldown: O(k)
# - Counter stores frequencies of k unique tasks: O(k) where k is the number of unique tasks

tasks = ["A","A","A","B","C"]
n = 3
print(leastInterval(tasks, n))  # Output: 9
tasks = ["X","X","Y","Y"]
n = 2
print(leastInterval(tasks, n))  # Output: 5