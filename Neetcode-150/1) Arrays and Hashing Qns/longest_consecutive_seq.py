# Longest Consecutive Sequence
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Convert list to hash set for O(1) lookups and calculate length only from numbers that are sequence starts

def longestConsecutive(nums):
    unique = set(nums)
    longest = 0
    for num in unique:
        if (num - 1) not in unique:
            length = 1
            while (num + length) in unique:
                length += 1
            longest = max(longest, length)
    return longest

# Time Complexity:
# - Converting list to set: O(n)
# - Iterating through the set of size n (in worst case): O(n)
#   - For each element, set lookup O(1), then we may enter the while loop
# - In total, all numbers are visited at most once, including the while loop: O(n)
# Space Complexity:
# - Set 'unique' stores all n elements: O(n)

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # Output: 4 

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))  # Output: 9 
