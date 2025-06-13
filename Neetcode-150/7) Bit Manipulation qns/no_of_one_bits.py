# Number of 1 Bits 
# Overall Time Complexity: O(k), where k is the number of set bits (1s) in n
# Overall Space Complexity: O(1)
# Hint: n & (n - 1) removes the lowest set bit from n in each iteration

def hammingWeight(n):
    result = 0
    while n:
        n = n & (n - 1)  
        result += 1
    return result

# Time Complexity:
# - Each iteration removes one set bit: O(1)
# - Loop runs k times, where k = number of set bits: O(k)
# - Total: O(k) ≤ O(32) → effectively O(1) for fixed-width integers
# Space Complexity:
# - Only a constant number of variables used: O(1)
# - No additional space needed

n = 0b00000000000000000000000000010111
print(hammingWeight(n))  # Output: 4
n = 0b1111111111111111111111111111101
print(hammingWeight(n))  # Output: 30