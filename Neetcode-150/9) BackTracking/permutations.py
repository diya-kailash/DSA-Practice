# Permutations
# Overall Time Complexity: O(n × n!)
# Overall Space Complexity: O(n), excluding the output space
# Hint: Use recursion - inserting the first element at every position of smaller permutations.

def permute(nums):
    if len(nums) == 0:
        return [[]]
    permutations = permute(nums[1:])  # Recurse on smaller list
    output = []
    for p in permutations:
        for i in range(len(p) + 1):
            p_copy = p.copy()              
            p_copy.insert(i, nums[0])      
            output.append(p_copy)
    return output

# Time Complexity:
# - There are n! total permutations of n elements
# - For each permutation, inserting the first element at all positions takes O(n) time in worst case
# - Total: O(n × n!)
# Space Complexity:
# - Recursion stack depth: O(n)
# - Each intermediate copy (p_copy) uses O(n) 
# - Output list stores n! permutations, each of size n: O(n × n!)
# - Total: O(n) excluding output space

nums = [1,2,3]
print(permute(nums))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums = [7]
print(permute(nums))  # Output: [[7]]