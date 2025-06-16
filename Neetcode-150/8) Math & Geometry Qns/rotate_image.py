# Rotate Image
# Overall Time Complexity: O(n^2)
# Overall Space Complexity: O(1)
# Hint: First transpose the matrix, then reverse each row

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
    for i in range(n):
        matrix[i].reverse() 

# Time Complexity:
# - Transpose: Two nested loops over n x n matrix → O(n^2)
# - Reverse each of n rows of length n → O(n^2)
# Space Complexity:
# - In-place operations only: O(1)
# - No extra space used
