# Subsets 
# Overall Time Complexity: O(n x 2^n)
# Overall Space Complexity: O(n), excluding the output space
# Hint: Use recursion to include or exclude each element, exploring all 2^n subsets

def subsets(nums):
    output = []
    def find_subsets(i, sub):
        if i == len(nums):
            output.append(sub.copy())  
            return 
        sub.append(nums[i])           # Include nums[i]
        find_subsets(i + 1, sub)
        sub.pop()                     # Backtrack and exclude nums[i]
        find_subsets(i + 1, sub)

    find_subsets(0, [])
    return output

# Time Complexity:
# - Each element has 2 choices (include or exclude): 2^n total subsets
# - Each subset takes up to O(n) time to copy into output
# - Total: O(n × 2^n)
# Space Complexity:
# - Recursion stack depth: O(n)
# - Output list stores 2^n subsets, each of size up to n: O(n × 2^n)
# - Total: O(n) excluding output space
