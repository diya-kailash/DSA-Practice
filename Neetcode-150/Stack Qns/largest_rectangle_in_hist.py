# Largest Rectangle in Histogram
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Monotonic stack keeps track of increasing heights; compute area on height drop

def largestRectangleArea(heights):
    stack = [] 
    max_area = 0
    for i in range(len(heights)):
        start = i
        while stack and heights[i] < stack[-1][1]:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, heights[i]))
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

# Time Complexity:
# - Each bar is pushed and popped from the stack at most once: O(n)
# - Area computation per pop: O(1)
# - Final pass over stack: O(n) in total 
# - Total: O(n)
# Space Complexity:
# - Stack stores at most n elements: O(n)
# - Constant extra space for variables like `max_area`, `start`: O(1)
# - Total: O(n)

heights = [7,1,7,2,2,4]
print(largestRectangleArea(heights))  # Output: 8
heights = [1,3,7]
print(largestRectangleArea(heights))  # Output: 7
