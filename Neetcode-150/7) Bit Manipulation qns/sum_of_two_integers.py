# Sum of Two Integers (without using + or -)
# Overall Time Complexity: O(1) 
# Overall Space Complexity: O(1)
# Hint: Use bitwise operations to simulate addition. XOR for sum, AND + Shift for carry

def getSum(a, b):
    mask = 0xFFFFFFFF                 
    max_int = 0x7FFFFFFF             
    while b != 0:
        carry = (a & b) << 1         
        a = (a ^ b) & mask           
        b = carry & mask             
    return a if a <= max_int else ~(a ^ mask)

# Time Complexity:
# - Loop runs at most 32 times for 32-bit integers: O(1)
# - All bitwise operations are constant time
# Space Complexity:
# - Constant space used for variables (a, b, mask, carry): O(1)
# - No additional data structures

a, b = 1, 1
print(getSum(a, b))  # Output: 2
a, b = 4, 7
print(getSum(a, b))  # Output: 11
a, b = -5, 3
print(getSum(a, b))  # Output: -2
