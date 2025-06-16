# Power Function 
# Overall Time Complexity: O(log n)
# Overall Space Complexity: O(1)
# Hint: Python's built-in exponentiation operator (**) 

def myPow(x, n):
    return x ** n

# Time Complexity:
# - Python’s `**` operator uses fast exponentiation (exponentiation by squaring)
# - Efficiently computes power in O(log n) time
# Space Complexity:
# - Uses constant extra space: O(1)

x = 2.00000
n = 5
print(myPow(x, n))  # Output: 32.0
x = 2.00000
n = -3
print(myPow(x, n))  # Output: 0.125
