# Counting Bits 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Number of 1s in i is number of 1s in i - offset, where offset is the most recent power of 2.

def countBits(n):
    dp = [0] * (n + 1)                  
    offset = 1                          
    for i in range(1, n + 1):
        if offset * 2 == i:            
            offset = i
        dp[i] = 1 + dp[i - offset]     
    return dp

# Time Complexity:
# - Loop runs from 1 to n: O(n)
# - All operations inside loop are O(1)
# Space Complexity:
# - dp array of size n+1: O(n)
# - Constant space for `offset`: O(1)

n = 4
print(countBits(n))  # Output: [0, 1, 1, 2, 1]
n = 7
print(countBits(n))  # Output: [0, 1, 1, 2, 1, 2, 2, 3]