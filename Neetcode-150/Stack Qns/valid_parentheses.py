# Valid Parentheses
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Use a stack to match opening and closing brackets

def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

# Time Complexity:
# - Each character is processed once: O(n)
#   - Stack operations (append and pop) are O(1)
# - Total: O(n), where n is the length of the string
# Space Complexity:
# - Stack stores at most all opening brackets in worst case: O(n)
#   - Mapping dictionary is constant size: O(1)
# - Total: O(n)

s = "([{}])"
print(isValid(s))  # Output: True
s = "([)]"
print(isValid(s))  # Output: False
