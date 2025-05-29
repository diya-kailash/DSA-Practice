# Daily Temperatures
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Monotonic stack is used to track indices of decreasing temperatures

def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and stack[-1][1] < temperatures[i]:
            index, temp = stack.pop()
            result[index] += i - index
        stack.append((i, temperatures[i]))
    return result

# Time Complexity:
# - Each temperature index is pushed and popped from the stack at most once: O(n)
# - Inner loop processes each element at most once due to monotonicity
# - Total: O(n)
# Space Complexity:
# - Stack stores indices and values (at most n elements): O(n)
# - Total: O(n)

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))  # Output: [1, 4, 1, 2, 1, 0, 0]
temperatures = [22,21,20]
print(dailyTemperatures(temperatures))  # Output: [0, 0, 0]