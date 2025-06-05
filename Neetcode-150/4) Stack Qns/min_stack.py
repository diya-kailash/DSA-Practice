# Min Stack
# Overall Time Complexity (for all operations): O(1)
# Overall Space Complexity: O(n)
# Hint: Use an auxiliary stack to track minimums for constant-time retrieval

class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) 
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

# Time Complexity:
# - push: O(1), because both append operations are constant time
# - pop: O(1), pops from both stacks in constant time
# - top: O(1), direct access to the top element
# - getMin: O(1), top of min_stack gives current minimum directly
# Space Complexity:
# - stack: stores all elements → O(n)
# - min_stack: also stores one entry per element (mirrors stack size) → O(n)
# - Total: O(n), where n is the number of elements pushed onto the stack

# Create the stack
minStack = MinStack()

minStack.push(5)      
minStack.push(3)      
minStack.push(7)     
minStack.push(2)      
print(minStack.getMin())  # Output: 2 
minStack.pop()          
print(minStack.getMin())  # Output: 3
print(minStack.top())     # Output: 7
minStack.pop()         
print(minStack.getMin())  # Output: 3
minStack.pop()          
print(minStack.getMin())  # Output: 5
