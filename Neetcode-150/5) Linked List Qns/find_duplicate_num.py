# Find Duplicate Number 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Use Floyd's tortoise and hare algorithm to detect cycle, then find cycle start

def findDuplicate(nums):
   slow, fast = 0, 0
   # Phase 1: Detect cycle using Floyd's algorithm
   while True:
       slow = nums[slow]
       fast = nums[nums[fast]]
       if fast == slow:
           break
   # Phase 2: Find start of cycle (duplicate number)
   slow2 = 0
   while True:
       slow = nums[slow]
       slow2 = nums[slow2]
       if slow2 == slow:
           return slow

# Time Complexity:
# - Phase 1 (cycle detection): O(n) - slow and fast pointers will meet within n iterations
# - Phase 2 (find cycle start): O(n) - finding entrance to cycle takes at most n steps
# - Total: O(n) where n is length of nums array
# Space Complexity:
# - Only constant space used for pointers (slow, fast, slow2): O(1)
# - No additional data structures created
