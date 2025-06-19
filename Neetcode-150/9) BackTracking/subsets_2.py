# Subsets With Duplicates 
# Overall Time Complexity: O(2^n × n)
# Overall Space Complexity: O(n), excluding the output space
# Hint: Explore all 2^n subsets and store them as tuples in a set to eliminate duplicates.

def subsetsWithDup(nums):
    output = set()
    nums.sort()
    def find_subsets(i, sub):
        if i == len(nums):
            output.add(tuple(sub))        
            return 
        sub.append(nums[i])              # Include nums[i]
        find_subsets(i + 1, sub)
        sub.pop()                        
        find_subsets(i + 1, sub)         # Exclude current element

    find_subsets(0, [])
    return [list(tup) for tup in output]

# Time Complexity:
# - Each element has two choices (include or exclude): O(2^n) subsets generated
# - Each subset takes O(n) time to copy as tuple and insert into set
# - Total: O(2^n × n)
# Space Complexity:
# - Recursion stack depth: O(n)
# - Temporary subset list used in recursion: O(n)
# - Output set stores up to 2^n subsets: O(2^n)
# - Total: O(n) excluding output space

nums = [1,2,1]
print(subsetsWithDup(nums))  # Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
nums = [7,7]
print(subsetsWithDup(nums))  # Output: [[],[7], [7,7]]
