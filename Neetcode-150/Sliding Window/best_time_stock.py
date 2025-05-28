# Best Time to Buy and Sell Stock 
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Sliding window (left and right pointers)

def maxProfit(prices):
    max_profit = 0
    l, r =  0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        else:
            l = r
        r += 1
    return max_profit

# Time Complexity:
# - Single pass using two pointers (`l` and `r`): O(n)
#   - Each element is visited at most once
#   - max and arithmetic operations per step: O(1)
# Space Complexity:
# - Only a few integer variables (`l`, `r`, `max_profit`, `profit`): O(1)
# - No extra memory used

prices = [10,1,5,6,7,1]
print(maxProfit(prices))  # Output: 6
prices = [10,8,7,5,2]
print(maxProfit(prices))  # Output: 0

