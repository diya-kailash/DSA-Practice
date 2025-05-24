# Container With Most Water
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Two-pointer technique

def maxArea(heights):
    max_area = 0
    i, j = 0, len(heights)-1
    while i < j:
        area = (j-i) * min(heights[i], heights[j])  
        max_area = max(max_area, area)  
        if heights[i] <= heights[j]:
            i += 1 
        else:
            j -= 1
    return max_area

# Time Complexity:
# - Two-pointer traversal: O(n)
#   - Each index is visited at most once as either `i` or `j` moves inward each step
#   - Area calculation and comparison: O(1) per step
# Space Complexity:
# - Uses a few integer variables (`max_area`, `i`, `j`, `area`): O(1)

height = [1,7,2,5,4,7,3,6]
print(maxArea(height))  # Output: 36
height = [2, 2, 2]
print(maxArea(height))  # Output: 4