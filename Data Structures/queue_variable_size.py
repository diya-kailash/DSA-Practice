# VARIABLE SIZE QUEUE 
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        item = self.items.pop(0)
        return item

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        for i in range(len(self.items)):
            print(self.items[i])

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()
queue.enqueue(40)
queue.display()
print(queue.size())

# VARIABLE SIZE QUEUE USING DEQUE
from collections import deque
class DequeQueue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        for item in self.items:
            print(item)

# Example usage 
deque_queue = DequeQueue()
deque_queue.enqueue(10)
deque_queue.enqueue(20)
deque_queue.enqueue(30)
deque_queue.display()
deque_queue.dequeue()
deque_queue.dequeue()
deque_queue.display()
deque_queue.enqueue(40)
deque_queue.display()
print(deque_queue.size())