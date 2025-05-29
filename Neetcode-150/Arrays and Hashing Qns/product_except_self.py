# Product of Array Except Self
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Use prefix and suffix products in two passes - forward and backward

def productExceptSelf(nums):
    output = [1] * len(nums)
    prefix = 1  
    for i in range(len(nums)):
        output[i] *= prefix
        prefix *= nums[i]
    suffix = 1  
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output

# Time Complexity:
# - First pass (left to right): O(n)
#   - For each element: O(1) operations
# - Second pass (right to left): O(n)
#   - For each element: O(1) operations
# Space Complexity:
# - Output array of size n: O(n)

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
