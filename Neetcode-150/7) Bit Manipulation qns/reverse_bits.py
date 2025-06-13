# Reverse Bits 
# # Overall Time Complexity: O(1)
# Overall Space Complexity: O(1)
# Hint: Iterate through each of the 32 bits, extract the i-th bit from `n`, and place it in the reversed position in `result`

def reverseBits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1                 
        result = result | (bit << (31 - i))  
    return result

# Time Complexity:
# - Fixed loop of 32 iterations: O(32) = O(1)
# - Bitwise operations are constant time: O(1)
# Space Complexity:
# - Constant variables used: result, bit: O(1)
# - No extra data structures

n = 0b00000000000000000000000000010101
print(reverseBits(n))  # Output: 2818572288

