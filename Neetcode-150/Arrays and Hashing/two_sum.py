# Two Sum
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Hash map to store numbers and their indices and checking for complements

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in hashmap:
            return [hashmap[rem], i]
        hashmap[nums[i]] = i

# Time Complexity:
# - Initializing empty dictionary: O(1)
# - Iterating through the list of size n: O(n)
#   - Calculating remainder: O(1)
#   - Dictionary lookup: O(1) average-case
#   - Inserting into dictionary: O(1) average-case

# Space Complexity:
# - Dictionary `hashmap` can store up to n elements in worst-case: O(n)

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # [0, 1]