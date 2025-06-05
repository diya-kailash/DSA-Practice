# Generate Parentheses
# Overall Time Complexity: O(4^n / √n)
# Overall Space Complexity: O(n) (for recursion stack) 
# Hint: Using stack + Backtracking approach to build valid combinations of parentheses

def generateParenthesis(n):
    output = []
    stack = []
    def recursive(open_count, close_count):
        if open_count == close_count == n:
            output.append("".join(stack))
            return
        if open_count < n:
            stack.append('(')
            recursive(open_count + 1, close_count)
            stack.pop()
        if close_count < open_count:
            stack.append(')')
            recursive(open_count, close_count + 1)
            stack.pop()
    recursive(0, 0)
    return output

# Time Complexity:
# - The total number of valid combinations of parentheses is the nth Catalan number: C(n) = O(4^n / √n)
# - Each combination takes O(n) time to build (string concatenation via stack)
# - Total: O(4^n / √n)
# Space Complexity:
# - Recursion stack goes as deep as 2n: O(n)
# - Total: O(n)

print(generateParenthesis(3))  # Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generateParenthesis(1))  # Output: ['()']