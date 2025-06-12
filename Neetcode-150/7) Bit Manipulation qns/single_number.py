# Single Number 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: XOR cancels out pairs (a ^ a = 0)

def singleNumber(nums):
    result = 0
    for num in nums:
        result = result ^ num      
    return result

# Time Complexity:
# - Iterate through all n elements: O(n)
# - XOR operation per element: O(1)
# Space Complexity:
# - Constant space used for `result`: O(1)
# - No additional data structures used
