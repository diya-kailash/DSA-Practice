# Spiral Matrix 
# Overall Time Complexity: O(n * m)
# Overall Space Complexity: O(1)
# Hint: Traverse layer by layer: top row → right col → bottom row → left col

def spiralOrder(matrix):
    output = []
    n, m = len(matrix), len(matrix[0])       
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for j in range(left, right + 1):
            output.append(matrix[top][j])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            output.append(matrix[i][right])
        right -= 1

        # Traverse from right to left along the bottom row (if still within bounds)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                output.append(matrix[bottom][j])
            bottom -= 1

        # Traverse from bottom to top along the left column (if still within bounds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

    return output

# Time Complexity:
# - Every element is visited exactly once: O(n * m)
# - n = number of rows, m = number of columns
# Space Complexity:
# - Constant extra space for pointers (top, bottom, left, right): O(1)
# - Output list stores all elements: O(n * m)
# - Total: O(1) excluding the output list
