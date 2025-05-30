# VARIABLE SIZE STACK
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements:")
        for item in reversed(self.items):
            print(item)

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
