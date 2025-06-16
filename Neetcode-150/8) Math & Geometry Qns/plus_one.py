# Plus One 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1) or O(n) (if carry causes extra digit)
# Hint: Simulate addition from the least significant digit

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Time Complexity:
# - Worst case: traverse all n digits when all are 9 (e.g., [9,9,9] → [1,0,0,0])
# - Each digit is processed once: O(n)
# Space Complexity:
# - In-place modification for most cases: O(1)
# - In worst case, one extra digit added (e.g., [9,9] → [1,0,0]): O(n) for output

digits = [1,2,3,4]
print(plusOne(digits))  # Output: [1, 2, 3, 5]
digits = [9,9,9]
print(plusOne(digits))  # Output: [1, 0, 0, 0]
