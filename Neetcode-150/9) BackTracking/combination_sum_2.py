# Combination Sum II (Unique Combinations)
# Overall Time Complexity: O(2^n × n)
# Overall Space Complexity: O(n), excluding the output space
# Hint: Recursively explore all subsets with backtracking while skipping duplicates using a set.

def combinationSum2(candidates, target) :
    output = set()
    candidates.sort()
    
    def find_combinations(i, s, sub):
        if s == target:
            output.add(tuple(sub))  
            return
        if i == len(candidates) or s > target:
            return 
        if s + candidates[i] <= target:
            sub.append(candidates[i])                  # Include candidates
            find_combinations(i + 1, s + candidates[i], sub)
            sub.pop()                                  
        find_combinations(i + 1, s, sub)               # Exclude current element

    find_combinations(0, 0, [])
    return [list(tup) for tup in output]

# Time Complexity:
# - In the worst case, for each element, we make two choices (include or exclude): O(2^n)
# - Each valid combination is copied to the set (conversion to tuple): O(n)
# - Total combinations processed and deduplicated: O(2^n × n)
# Space Complexity:
# - Recursion stack depth: O(n) in worst case (if all elements are used)
# - Sub list used in backtracking: O(n)
# - Output set stores up to 2^n combinations: O(2^n)
# - Total: O(n) excluding output space

candidates = [9,2,2,4,6,1,5]
target = 8
print(combinationSum2(candidates, target)) # Output: [[1,2,5], [2,2,4], [2,6]]
candidates = [1,2,3,4,5]
target = 7
print(combinationSum2(candidates, target)) # Output: [[1, 2, 4], [2, 5], [3, 4]]

