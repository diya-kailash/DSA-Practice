# Find Kth Largest Element in an Array 
# Overall Time Complexity: O(n log k)
# Overall Space Complexity: O(k)
# Hint: Use Python’s built-in heapq.nlargest to get the k largest elements, then return the last one

import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]  

# Time Complexity:
# - heapq.nlargest uses a min-heap of size k internally
# - For each of the n elements: insertion/check into heap of size k: O(log k)
# - Total: O(n log k)
# Space Complexity:
# - Internal heap of size k used by heapq.nlargest: O(k)
# - The list returned by heapq.nlargest contains k elements: O(k)

nums = [2,3,1,5,4]
k = 2
print(findKthLargest(nums, k))  # Output: 4
nums = [2,3,1,1,5,5,4]
k = 3
print(findKthLargest(nums, k))  # Output: 4