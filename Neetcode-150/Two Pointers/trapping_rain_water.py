# Trapping Rain Water
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Two-pointer technique

def trap(height):
    if not height:
        return 0
    max_area = 0
    i, j = 0, len(height)-1
    left_max, right_max = height[i], height[j]
    while i < j:
        if left_max <= right_max:
            i += 1
            left_max = max(left_max, height[i])
            max_area += left_max - height[i]
        else:
            j -= 1
            right_max  = max(right_max, height[j])
            max_area += right_max - height[j]
    return max_area

# Time Complexity:
# - Single pass using two pointers: O(n)
#   - Each element is visited at most once
#   - max operations and arithmetic per step: O(1)
# Space Complexity:
# - Only a few integer variables (`i`, `j`, `left_max`, `right_max`, `max_area`): O(1)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6
height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))  # Output: 9

