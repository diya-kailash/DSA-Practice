# Sliding Window Maximum
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(k)
# Hint: Use a deque to store indices of useful elements in the current window

import collections
def maxSlidingWindow(nums, k):
    output = []
    queue = collections.deque()
    l = r = 0
    while r < len(nums):
        while queue and nums[r] > nums[queue[-1]]:
            queue.pop()
        queue.append(r)
        if l > queue[0]:
            queue.popleft()
        if (r + 1) >= k:
            output.append(nums[queue[0]])
            l += 1
        r += 1
    return output

# Time Complexity:
# - Each element is added to and removed from deque at most once: O(n)
# - Appending to result array happens n - k + 1 times: O(n)
# - Total: O(n), where n = len(nums)
# Space Complexity:
# - Deque stores at most k elements (indices): O(k)
# - Output list stores n - k + 1 elements: O(n) (if included)
# - Total (excluding output): O(k)

nums = [1,2,1,0,4,2,6]
k = 3
print(maxSlidingWindow(nums, k)) # Output: [2, 2, 4, 4, 6]
nums = [1, -1]  
k = 1
print(maxSlidingWindow(nums, k))  # Output: [1, -1]
