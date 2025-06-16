# Happy Number
# Overall Time Complexity: O(log n) per iteration × number of iterations (bounded)
# Overall Space Complexity: O(log n) × number of unique intermediate numbers (bounded)
# Hint: Use a set to detect cycles while computing sum of squares of digits

def sum_of_squares(n):
    s = 0
    while n:
        d = n % 10
        s += (d ** 2)
        n = n // 10
    return s

def isHappy(n):
    visited = set()
    while n not in visited:
        visited.add(n)
        n = sum_of_squares(n)
        if n == 1:
            return True
    return False

# Time Complexity:
# - Each call to `sum_of_squares`: O(log n) 
# - Number of iterations, k is bounded (the process converges or loops over a small cycle)
# - Total: O(log n) per iteration × O(k) iterations
# Space Complexity:
# - Visited set stores previous numbers: O(k)
# - Each number is at most O(log n) digits
# - Total: O(log n) × O(k) = O(log n) in practice, since k is small and bounded

n = 100
print(isHappy(n))  # Output: True
n = 101
print(isHappy(n))  # Output: False