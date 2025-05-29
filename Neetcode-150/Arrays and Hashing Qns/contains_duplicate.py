# Contains Duplicate 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Hash set to track duplicates

def hasDuplicate(nums):
    unique = set()
    for x in nums:
        if x in unique:
            return True
        unique.add(x)
    return False

# Time Complexity:
# - Initializing an empty set: O(1)
# - Iterating through the list of size n: O(n)
#   - For each element:
#       - Checking membership in a set: O(1) average-case
#       - Adding to a set: O(1) average-case
# Space Complexity:
# - Set 'unique' can grow up to size n in worst-case (no duplicates): O(n)

nums = [1, 2, 3, 4]
print(hasDuplicate(nums)) # False
nums = [1, 2, 3, 1] 
print(hasDuplicate(nums)) # True