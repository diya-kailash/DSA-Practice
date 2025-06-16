# Multiply Strings 
# Overall Time Complexity: O(n + m)
# Overall Space Complexity: O(n + m)
# Hint: Convert strings to integers, multiply, then convert back to string

def multiply(num1, num2):
    return str(int(num1) * int(num2))

# Time Complexity:
# - Converting num1 and num2 to integers: O(n) and O(m) respectively, where n and m are lengths of the input strings
# - Multiplying two integers of length n and m: O(n * m) in general (though Python uses optimized algorithms internally)
# - Converting result back to string: O(n + m) in the worst case
# Space Complexity:
# - Temporary integer representations of the inputs and output: O(n + m)
# - Final output string: O(n + m)

num1 = "3"
num2 = "4"
print(multiply(num1, num2))  # Output: "12"
num1 = "111"
num2 = "222"
print(multiply(num1, num2))  # Output: "24642"