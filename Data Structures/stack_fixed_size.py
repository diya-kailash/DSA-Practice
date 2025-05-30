# FIXED SIZE STACK
class Stack:
    def __init__(self, max_size=10):
        self.items = [None] * max_size  
        self.top = -1
        self.max_size = max_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.items[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[self.top]

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements:")
        for i in range(self.top, -1, -1):
            print(self.items[i])

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()
stack.push(40)
stack.display()
stack.pop()
print(stack.peek())
print(stack.size())

