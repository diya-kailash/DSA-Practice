# Reverse Integer
# Overall Time Complexity: O(1)
# Overall Space Complexity: O(1)
# Hint: Repeatedly extract last digit and construct reversed number. Handle overflow.

import math
def reverse(x) -> int:
    MIN = -2147483648  # -2^31
    MAX = 2147483647   #  2^31 - 1
    result = 0
    while x:
        digit = int(math.fmod(x, 10))  
        x = int(x / 10)               
        if result > MAX // 10 or (result == MAX // 10 and digit > MAX % 10):
            return 0
        if result < MIN // 10 or (result == MIN // 10 and digit < MIN % 10):
            return 0
        result = (result * 10) + digit
    return result

# Time Complexity:
# - Each iteration removes a digit, and the number of digits is log(x): O(log(x)) 
# - Constant time operations inside the loop: O(1)
# - Total: O(log(x)), but since x is bounded by 32-bit integer limits, we can consider it O(1)
# Space Complexity:
# - Constant space used for variables (result, digit, x, MIN, MAX): O(1)
# - No additional data structures used

x = 1234
print(reverse(x))  # Output: 4321
x = -1234
print(reverse(x))  # Output: -4321
x = 1234236467
print(reverse(x))  # Output: 0 (overflow)
