# Set Matrix Zeroes 
# Overall Time Complexity: O(n * m)
# Overall Space Complexity: O(n + m)
# Hint: First collect all rows and columns that need to be zeroed, then update matrix accordingly

def setZeroes(matrix):
    rows = []
    cols = []
    n, m = len(matrix), len(matrix[0])  
    # First pass: identify rows and columns to be zeroed
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    # Second pass: set elements to zero if in marked row or column
    for i in range(n):
        for j in range(m):
            if i in rows or j in cols:
                matrix[i][j] = 0

# Time Complexity:
# - First pass over the matrix to find zeroes: O(n * m)
# - Second pass to update elements: O(n * m)
# - Total: O(n * m), where n is the number of rows and m is the number of columns
# Space Complexity:
# - Space for storing row and column indices: O(n + m) in the worst case
