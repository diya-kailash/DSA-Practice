# Evaluate Reverse Polish Notation (RPN) - same as postfix notation
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: Use a stack to evaluate the expression 

def evalRPN(tokens):
    stack = []
    for ch in tokens:
        if ch == "+":
            stack.append(stack.pop() + stack.pop())
        elif ch == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif ch == "*":
            stack.append(stack.pop() * stack.pop())
        elif ch == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))  
        else:
            stack.append(int(ch))
    return stack.pop()

# Time Complexity:
# - Iterates through all `n` tokens once: O(n)
# - Each operation (push, pop, arithmetic) takes constant time: O(1)
# - Total: O(n)
# Space Complexity:
# - Uses a stack to store operands: at most O(n) in worst case (all numbers)
# - No additional space beyond the stack
# - Total: O(n)

tokens = ["1","2","+","3","*","4","-"]
print(evalRPN(tokens))  # Output: 5
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))  # Output: 9