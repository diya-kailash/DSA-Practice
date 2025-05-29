# Two Sum in Sorted Array
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Two-pointer technique - i at beginning and j at end, move inward

def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return [i + 1, j + 1]
    return []

# Time Complexity:
# - Scans each character at most once: O(n)
#   - Comparing sums: O(1)
# Space Complexity:
# - Uses only a few integer variables (i, j): O(1)

numbers = [1,2,3,4]
target = 3
print(twoSum(numbers, target))  # Output: [1, 2]
numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))  # Output: [1, 3]

