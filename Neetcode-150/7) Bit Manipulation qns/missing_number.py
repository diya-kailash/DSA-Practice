# Missing Number
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Using XOR, pairs cancel out, leaving the missing number

def missingNumber(nums):
    n = len(nums)
    missing = n                             
    for i in range(n):
        missing ^= i ^ nums[i]              
    return missing

# Time Complexity:
# - Loop over n elements: O(n)
# - Constant-time XOR operations per iteration: O(1)
# Space Complexity:
# - Only constant space used (missing, i): O(1)
# - No additional data structures

nums = [1,2,3]
print(missingNumber(nums))  # Output: 0
nums = [3,0,1]
print(missingNumber(nums))  # Output: 2
