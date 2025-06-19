# Combination Sum 
# Overall Time Complexity: O(2^t), where t = target 
# Overall Space Complexity: O(t) for recursion stack
# Hint: Try including the current number multiple times, and skip to next when needed

def combinationSum(nums, target):
    output = []
    def find_combinations(i, s, sub):
        if s == target:
            output.append(sub.copy())     
            return
        if i == len(nums) or s > target:
            return
        if s + nums[i] <= target:
            sub.append(nums[i])           # Include current number
            find_combinations(i, s + nums[i], sub)  
            sub.pop()                  
        find_combinations(i + 1, s, sub)  # Exclude and move to next number

    find_combinations(0, 0, [])
    return output

# Time Complexity:
# - Exponential in worst case due to the number of combinations: O(2^t) for target t (t/m, where m is min(nums))
# - Each recursive call can branch in 2 ways: include or exclude current element
# - Copying subset when target is met: O(k) where k is the average length of subset
# - Total: O(2^t) in worst case
# Space Complexity:
# - Recursion stack depth up to O(t) in worst case (max depth = t/m)
# - Output stores all valid combinations: O(k)
# - Total: O(t), excluding output space

nums = [2,5,6,9] 
target = 9
print(combinationSum(nums, target)) # Output: [[2,2,5],[9]]

nums = [3,4,5]
target = 16
print(combinationSum(nums, target)) # Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
